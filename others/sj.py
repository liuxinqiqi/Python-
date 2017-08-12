#coding=utf-8
'''题目要求：现在有一个文件夹myDir，该文件夹中又有n个文件夹dir1,Dir2, ..., dir
N，每个文件夹中又有m个文件，这个实例需要达到的目的就是要将这n个文件夹dir1,D
ir2, ..., dirN中的所有文件全部写到一个新文件中，该新文件在文件夹myDir下。

1.找一个目录下的所有文件
2.将文件中的内容取出
3.将所有内容写入一个文件中
 '''

import os
def sj(rootDir,outPutFile):
    fw = open(outPutFile,'w')
    for dirName in os.listdir(rootDir):
        if os.path.isdir(os.path.join(rootDir,dirName)):
            print 'process in dir:%s'%dirName
            for fileName in os.listdir(os.path.join(rootDir,dirName)):
                if os.path.isfile(os.path.join(rootDir,os.path.join(dirName,fileName))):
                    fr = open(os.path.join(rootDir,os.path.join(dirName,fileName)),'r')
                    for eachline in fr:
                        fw.write(eachline)
                    fr.close()
    fw.close()
sj('myDir','all.txt')
