#coding=utf-8

f = open("file2",'w+')

f.writelines(['hello\n','world\n','1\n','2\n'])   #手动换行

f.writelines("我住长江头，君住长江尾。\n日日思君不见君，共饮长江水。\n此水几时休，此恨何时已。\n只愿君心似我心，定不负相思意。")
