#coding=utf-8
import sys

with open('file1','r+') as f:
    print >> f, "撑着油纸伞的女孩"    # 写入f
print >> sys.stdout, "独自彷徨"
print >> sys.stderr, "雨巷"
# print >>sys.stdin,"悠长"          #不能输入
