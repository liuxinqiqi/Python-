#coding=utf-8

f = open('hold','w')
f.write('b')
f.seek(1024*1024*3)     #占用空间
f.write('e')           #空洞文件
