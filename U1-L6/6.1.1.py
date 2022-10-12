a="abc"
a=a.replace("a"," ")
print(a)
print("0".join(a))#join相当于sep
b="     j       "
print(b.strip())
print(b.lstrip())#会删除所有匹配的字符 比如指定"今天",那么就会把所有"今"和"天"字逐一删除
print(b.rstrip())
c="dasdhasjkdhas"#用于三等分，返回一个元组，括号中写中间部分的
print(c.partition("has"))#partition选择的是前一个has    返回元组
print(c.rpartition("has"))#partition选择的是后一个has    返回元组
print(c.split("j"))#这里是把j作为分隔符，把字符串分成两部分    返回列表    遍历删除
print(c.rsplit("a"))#从右侧开始分割，如果不指定max，效果与split相同，如果指定max（最大分割次数），就与split的不同    返回列表    遍历删除
print(b.removeprefix("    "))#修剪左边，括号中写想要减去的部分  整体删除 只会删除指定的前缀，与lstrip不同
print(b.removesuffix("     "))#修剪右边，括号中写想要减去的部分 整体删除
d="123\n456\r789\t101112"
print(d.splitlines())#在换行符(\n,\r,\t)处拆分字符串并,空格不算    返回列表
a="aaabbbcccddddd"
print(a.count("a"))#返回查找到的次数
print(a.find("a"))#返回查找到的位置（如果有多个就返回第一个），如果没找到返回-1，但是index会error
print(a.startswith("a"))#如果以指定字符串开始，返回true
print(a.endswith("d"))#如果以指定字符结束，返回True
f="   "
print(f.isspace())#如果字符串中所有字符都是空白字符，则返回true
print(a.isalpha())#如果字符串中所有字符都是字母表中的字符，则返回true
num="12212"
print(num.isalnum())#如果字符串中所有元素都是字母数字，则返回true
Cap="CAPITAL"
print(Cap.isupper())#如果字符串中所有字符都是大写，则返回True
notcap="amkamzaz"
print(notcap.islower())#如果字符串中所有字符都是小写，则返回true
print(notcap.upper())#变大写
print(Cap.lower())#变小写

