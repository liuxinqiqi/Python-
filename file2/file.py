#coding=utf-8
import os
import shutil
#
# print dir(os)
# print "-------------------------"
# print dir(os.path)
# print "-------------------------"
# print dir(shutil)


print os.getcwd()     #获取当前工作目录

# os.remove('hold')   #删除

print "-------------------------"
print os.path.isfile('file')     #判断是不是一个文件
print os.path.isdir('file')     #判断是不是一个文件夹
print os.path.exists('file')    #判断file文件是否存在
os.system('ls -l')          # 显示当前信息

# os.rename('csvfile.xls','test.xls')
# os.mkdir('dir')
print os.path.abspath(__file__)        # 获取文件的当前的绝对路径
print os.path.dirname(os.path.abspath(__file__))  #获取当前文件所在的的目录的绝对路径
print os.path.getsize('file')   #获取文件大小
print os.listdir('.') #获取当前文件夹下的所有文件
print os.path.join('/a/b/c','filename')   #拼接路径

shutil.copyfile('file','filenew')  # 复制file
shutil.move('a','b')   #移动，b可增加路径
shutil.copy('a','b')    # 复制，可复制文件夹
