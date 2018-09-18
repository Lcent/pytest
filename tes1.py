#!/usr/bin/python
# _*_ coding:utf-8 _*_

# 先打开一个有内容的文件
# 再打开一个空文件
# 将文件内容写入空文件
# 关闭两个文件
f = open("file.txt", "r")
cop = f.read()
nf = open("file-new.txt","w")
nf.write(cop)

f.close()
nf.close()
