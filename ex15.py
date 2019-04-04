# -*- coding: UTF-8 -*-

# 引入模块 argv
from sys import argv

# 解构 script、filename 获取filename
script, filename = argv

# 打开这个文件
text = open(filename)

print "Here's your file %r:" % filename

# 打印出文件的内容
print text.read()

text.close()

print "Type the filename again:"

file_again =  raw_input("> ")

text_again =  open(file_again)

print text_again.read()

text_again.close()