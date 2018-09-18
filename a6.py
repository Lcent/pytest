#!/usr/bin/python
# _*_ utf-8 _*_

# sum = 0
# for i in range(1, 11):
#     sum = sum + 1
# print(sum)

# 九九乘法表

# for i in range(1, 10):
#     # print(i)
#     for j in range(1, i+1):
#        # print(j)
#        print("%s * %s = %s" % (i, j, i*j), end="\t")
#     print()


# 斐波那切数列
# l2 = [2, 3]
# # # l2.append(l2[-1] + l2[-2])
# # # print(l2)

# l1 = [1, 2]
#
# for i in range(8):
#     l1.append(l1[-1] + l1[-2])
# print(l1)


# 循环菜单
# n = ''
# prompt = """
#    1.aaaa
#    2.bbbb
#    3.ccccc
#    """
# while not n:
#     print("nnnnn")
#     n = input(prompt)
#     if n == '1':
#         print("aaaa")
#     elif n == '2':
#         print("bbbb")
#     else:
#         print("ccccc")


# x = ''
# while x != 'q':
#     print('a')
#     x = input("plz:")
#  #  if x == " ":
#     if not x:
#         break
# else:
#         print('end')



# 登陆
# count = 0
# username = input("name:")
# password = input("password:")
# while True:
#     if username !='tom' and password !='123':
#         print("ok")
#         break
#     else:
#         count = count + 1
#         print("shibai%sci"%count)
#     # username = input("name:")
#     # password = input("password:")
#     if count == 2:
#         break
#

#  取内存总量
# f =  open('/proc/meminfo', 'r')
#
# for lines in f:
#     if lines.startswith("MemTotal"):
#         memtotal = int(lines.split()[1])/ 1024
#     if lines.startswith("MemFree:"):
#         memfree = int(lines.split()[1])/ 1024
#         break
# print("Used%.2fG - %.2fG = %.2fG" %(memtotal , memfree, memtotal - memfree))




# 拷贝文件
# s_file = '/usr/bin/ls'  # 源文件
# d_file = '/home/sl'     # 目标文件
# buffer_size = 4096
# s_obj_file = open(s_file, 'rb')
#
# d_obl_file = open(d_file, 'wb')
#
# while True:
#     data = s_obj_file.read()
#     if not data:
#         break
#     d_obl_file.write(data)
#     s_obj_file.close()
#     d_obl_file.close()


# 四则运算mod
# """size
#
# 加  减  乘  除
# """
# def jia(x, y):
#     return "%s + %s = %s" %(x, y, x + y)
#
# def jian(x, y)
#     return "%s - %s = %s" %(x, y, x - y)
#
# def cheng(x, y)
#     return "%s * %s = %s" %(x, y, x * y)
#
# def chu(x, y)
#     return "%s / %s = %s" %(x, y, x / y)




# 异常处理
# try:
#     fh = open("testfile", "w")
#     fh.write("这是一个测试文件，用于测试异常")
# except IOError:
#     print("Error: 没有找到文件或读取文件失败")
# else:
#     print("内容写入文件成功")
#     fh.close()



# try:
#     fh = open("testfile", "w")
#     fh.write("这是个测试文件，用于测试异常")
# except IOError:
#     print("Error:没有找到文件或者读取文件失败")
# else:
#     print("内容写入文件成功")
#     fh.close()


# try:
#     fh = open("testfile", "w")
#     fh.write("这是个测试文件，用于测试异常")
# finally:
#     print("Error: 没有找到文件或者读取文件失败")



# try:
#     fh = open("testfile","w")
#     try:
#         fh.write("这是一个测试文件，用于测试异常")
#     finally:
#         print("关闭文件")
#         fh.close()
# except IOError:
#     print("Error:没有找到文件或者读取文件失败")

# ***********************************************
# 循环
# if

# var1 = 100
# if var1:
#     print("1 - if 表达式条件为true")
#     print(var1)
#
# var2 = 0
# if var2:
#     print("2 - if 表达式条件为 true")
#     print(var2)
# print("Good bye!")

# *********************************************
# 狗的年龄计算判断
# age  = int(input("请输入你家狗狗的年龄："))
# print("")
# if age < 0:
#     print("你是在逗我吧！")
# elif age == 1:
#     print("相当于14岁的人。")
# elif age == 2:
#     print("相当于22岁的人。")
# elif age > 2:
#     human = 22 + (age -2)*5
#     print("对应人类的年龄：", human)
#
# ### 退出提示
# input("点击 enter 键退出")

# **********************************
# # 程序演示了 == 操作符
# # 使用数字
# print(5 == 6)
# # 使用变量
# x = 5
# y = 8
# print(x == y)
# **************************************
# # 猜数字游戏
# number = 7
# guess = -1
# print("数字猜谜游戏！")
# while guess != number:
#     guess = int(input("请输入你猜的数字:"))
#
#     if guess == number:
#         print("恭喜，你猜对了！")
#     elif guess < number:
#         print("猜的数字小了。。。")
#     elif guess > number:
#         print("猜的数字大了。。。")

# ********************************

# num=int(input("输入一个数字："))
# if num%2==0:
#     if num%3==0:
#         print("你输入的数字可以整除 2 和 3")
#     else:
#         print("你输入的数字可以整除 2，但不能整除 3")
# else:
#     if num%3==0:
#         print("你输入的数字可以整除 3，但不能整除 2")
#     else:
#         print("你输入的数字不能整除 2 和 3")

# *******************************

