import re
import sys
import getopt

create_string = """CREATE TABLE `RealCustomers` (
  `cust_id` int(10) NOT NULL AUTO_INCREMENT,
  `cust_name` char(50) NOT NULL,
  `cust_address` char(50) DEFAULT NULL,
  `cust_city` char(50) DEFAULT NULL,
  `cust_state` char(5) DEFAULT NULL,
  `cust_zip` char(10) DEFAULT NULL,
  `cust_country` char(50) DEFAULT NULL,
  `cust_contact` char(50) DEFAULT NULL,
  `cust_email` char(255) DEFAULT NULL,
  PRIMARY KEY (`cust_id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;\n"""



try:
    opts , arg = getopt.getopt(sys.argv[1:],'hf:s:o:')
except Exception as e:
    print 'Your input format is wrong!Please type in again!'
    sys.exit()

for opt , value in opts:
    if opt == '-f':
        CustomersFile = open(value)
    if opt == '-s':
        CustomersEmailFile = open(value)
    if opt == '-o':
        RealCustomersFile = open(value,'w+')
    if opt == '-h':
        print '---------     Usage:    ----------' 
        print '--'
        print '--   -f:    input file1    required   '
        print '--   -s:    input file2    required   '
        print '--   -o:    output file    required   '
        print '--'
        print '-- example:  python combine.py -f firstfile.sql -s secondfile.sql -o outputfile.sql'
        print '--'
        sys.exit()

CustomersInfoList = []
CustomersEmailList = []

insertPattern = re.compile(r'^INSERT INTO ')
dataPattern = re.compile(r'\((.+?)\)')


for line in CustomersFile.readlines():
    if insertPattern.match(line):
        data = dataPattern.findall(line)
        for simple_data in data:
            simple_data_list = simple_data.split(',')
            CustomersInfoList.append(simple_data_list[:])

for line in CustomersEmailFile.readlines():
    if insertPattern.match(line):
        data = dataPattern.findall(line)
        for simple_data in data:
            simple_data_list = simple_data.split(',')
            CustomersEmailList.append(simple_data_list[:])
i = 0
for info in CustomersInfoList:
    info.append(CustomersEmailList[i][1])
    i = i + 1



NewDatabaseString = "DROP TABLE IF EXISTS `RealCustomers`;\n"
NewDatabaseString = NewDatabaseString + create_string
NewDatabaseString = NewDatabaseString + "LOCK TABLES `RealCustomers` WRITE;\n"
NewDatabaseString = NewDatabaseString + "INSERT INTO `RealCustomers` VALUES "
for info in CustomersInfoList:
    info_string = ','.join(info)
    NewDatabaseString = NewDatabaseString + "(" + info_string + "),"
print len(NewDatabaseString)
NewDatabaseString2 = NewDatabaseString[0:len(NewDatabaseString) - 1]
NewDatabaseString2 = NewDatabaseString2 + ";\n" 
NewDatabaseString2 = NewDatabaseString2 + "UNLOCK TABLES;\n" 


RealCustomersFile.write(NewDatabaseString2)


CustomersFile.close()
CustomersEmailFile.close()
RealCustomersFile.close()
