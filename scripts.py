import MySQLdb
import random


ADDRESS = ['Mozhoudonglu','Jiangnanxilu','Hexiehuayuan','Donandaxue','Xiandianzikeji','Alibaba','Tecent']
CITY = ['JiNan','NanJing','BeiJing','XiangGang','Japan','Dali']
STATE = ['AAAA','BBBB','CCCCC','DDDD','EEEE','FFFF']

conn = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='wangyongjian3',db='for_scripts_test')

cur = conn.cursor()

execString = "DROP TABLE IF EXISTS Customers;\
        CREATE TABLE Customers \
       (cust_id      int(10)  NOT NULL auto_increment,\
        cust_name    char(50)  NOT NULL ,\
        cust_address char(50)  NULL ,\
        cust_city    char(50)  NULL ,\
        cust_state   char(5)   NULL ,\
        cust_zip     char(10)  NULL ,\
        cust_country char(50)  NULL ,\
        cust_contact char(50)  NULL ,\
        primary key (cust_id)) ;"

for i in range(1,10000):
    addressNum = random.randint(0,len(ADDRESS) - 1)
    cityNum = random.randint(0,len(CITY) - 1)
    stateNum = random.randint(0,len(STATE) - 1)
    name = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz',random.randint(3,7)))
    name = name.capitalize()
    insertString = "insert into Customers(cust_name,cust_address,cust_city,cust_state) \
            values( '%s' , '%s' , '%s' , '%s' );" % (name,ADDRESS[addressNum],CITY[cityNum],STATE[stateNum])
    global execString
    execString = execString + insertString
    if i == 99:
        print insertString
try:
    cur.execute(execString)
except Exception as e:
    print 'Error Appears in Insert table:%s' % e

cur.close()

conn.commit()

conn.close()

