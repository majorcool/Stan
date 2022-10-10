str1="hello python"
str2='我的外号是"大西瓜"'
print(str2)
print(str1[6])#可以直接从字符串里挑，比如这里strl[6]就会选取str1中的"p"
for char in str2:
    print(char)
hello_str="hello hello"
#统计字符串长度
print(len(hello_str))
#统计某个小字符串出现的次数
print(hello_str.count("h"))
#某一个子字符串出现的为重
print(hello_str.index("h"))
hello_str=""
#判断空白字符
space_str="   \t\n\r  "
print(space_str.isspace())
#判断字符串中是否只包含数字
#三种方法都不能判断小数
#Unicode字符串
num_str='1'
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())#功能较为强大(能判断中文数字)
#判断是否以指定字符串开始
print(hello_str.startswith("hello"))
#判断是否以指定字符串结束
print(hello_str.endswith("world"))
#查找指定字符串 find没找到不会报错，会返回-1，index会报错
print(hello_str.find("llo"))
#替换字符串
#replace方法执行完成之后会返回一个新的字符串，但是并不会修改原来的字符串
print(hello_str.replace("world","python"))

#假设：以下内容是从网络上抓取的
#要求：顺序并且居中对其输出以下内容
poem=["登鹤雀楼",
      "王之涣",
      "白日依山尽\t\n",
      "黄河入海流",
      "欲穷千里目",
      "更上一层楼"
      ]
for poem_str in poem:
    print("|%s|" % poem_str.center(10," "))
for poem_str in poem:
    print("|%s|" % poem_str.ljust(10," "))
for poem_str in poem:
    print("|%s|" % poem_str.rjust(10," "))
for poem_str in poem:
    #先使用strip方法去除字符串中的空白字符
    #再使用center居中显示
    print("|%s|" % poem_str.strip().center(10," "))
#拆分字符串(不指定拆分字符就默认在空格处拆分(\n\t这种也算空格)
str_e="sda asd asd asdc caxc c"
temp=str_e.split()
print(temp)
#合并字符串
result=" ".join(str_e)
print(result)
num_str="0123456789"
#1 切2-5
num_str[2:6]
#2切2-结尾
num_str[2:]
#30-5
num_str[0:6]
num_str[:6]
#4
num_str[:]
#5隔一个切一个
num_str[::2]
#6
num_str[1::2]
#7
num_str[2:-1]
#8
num_str[-2:]
#9 逆序时开始索引也可以省略
num_str[::-1]