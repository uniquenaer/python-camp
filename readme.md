# Python 入门

## python2 

### 字符串格式化

[Python补充05 字符串格式化 (%操作符) - Vamei - 博客园](http://www.cnblogs.com/vamei/archive/2013/03/12/2954938.html)

#### 格式符

%s    字符串 (采用str()的显示)

%r    字符串 (采用repr()的显示)

%c    单个字符

%b    二进制整数

%d    十进制整数

%i    十进制整数

%o    八进制整数

%x    十六进制整数

%e    指数 (基底写为e)

%E    指数 (基底写为E)

%f    浮点数

%F    浮点数，与上相同

%g    指数(e)或浮点数 (根据显示长度)

%G    指数(E)或浮点数 (根据显示长度)
 

%%    字符"%"

#### 语法

```python

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)

print formatter % ("one", "two" ,"three" , "four")


```

### raw_input

> 获取控制台的输入


#### 函数语法

raw_input([prompt])

prompt: 可选，字符串，可作为一个提示语。

```python

>>>a = raw_input("input:")
input:123

>>> type(a)
<type 'str'> 

```

### 参数、解包、变量

### 读写文件

close 关闭文件

read 读取文件内容

readline 读取文本文件第一行

truncate 清空文件

write(stuff)  将stuff写入文件

## Python3

### 变量

```python
my_chinese_name = "nana"

my_name = "Zed A. Shaw"

print(f"{my_chinese_name}")

print(f"Let's talk about {my_name}.")

hilarious = False

joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

```