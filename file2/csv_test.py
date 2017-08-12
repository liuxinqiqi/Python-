#coding=utf-8
import csv
try:
    f = open('csvfile.ods','rb')
except Exception as e:
    print 'open failed'
print dir(csv)
reader = csv.reader(open('csvfile.ods','rb'))
for line in reader:
    print line






import csv
# writer = csv.writer(open('csvfile.xls','wb'))       #写入
reader = csv.reader(open('csvfile.xls','rb'))          #读取
# writer.writerow(['a','b','c'])                       #以列表写入
for line in reader:
    print line
