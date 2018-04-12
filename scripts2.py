
import MySQLdb
import random


ADDRESS = ['Mozhoudonglu','Jiangnanxilu','Hexiehuayuan','Donandaxue','Xiandianzikeji','Alibaba','Tecent']
CITY = ['JiNan','NanJing','BeiJing','XiangGang','Japan','Dali']
STATE = ['AAAA','BBBB','CCCCC','DDDD','EEEE','FFFF']
EMAIL = ['163','qq','google','yahoo','sina','alibaba','tecent']
conn = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='wangyongjian3',db='for_scripts_test')

cur = conn.cursor()

execString = "DROP TABLE IF EXISTS CustomersEmail;\
        CREATE TABLE CustomersEmail \
       (cust_id      int(10)  NOT NULL auto_increment,\
        cust_email char(255)  NULL ,\
        primary key (cust_id)) ;"

for i in range(1,10000):
    content = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz1234567890',random.randint(5,15)))
    content = content + '@' + EMAIL[random.randint(0,len(EMAIL) - 1)] + '.com'
    insertString = "insert into CustomersEmail(cust_email) \
            values( '%s' );" % content
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

