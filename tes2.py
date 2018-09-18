#!/usr/bin/python
# _*_ coding:utf-8 _*_

# 导入os模块
# 通过模块进行创建文件或目录
import os
os.mkdir("new_file")
f = open("file.txt", "w")
f.close()