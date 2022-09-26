name_list= ["zhangsan", "lisi", "wangwu"]
#1.取值和取索引
print(name_list[0])
#知道数据的内容，想确定数据在列表中的位置
print(name_list.index("wangwu"))

#2.修改
name_list[1]="李四"
#list assignment index out of range
#列表指定的索引超出范围，程序会报错!
name_list[3]="ll"

#3.增加
#append 方法可以向列表的末尾追加数据
name_list.append("LBW")
name_list.insert(1,"LLLL")
#这里insert(插入的位置,插入的值)
temp_list=["SWK","ZEG","SSD"]
name_list.extend(temp_list)
#extend可以把一个列表追加到另一个列表的末尾

#4删除
name_list.remove("wangwu")
#pop默认移除最后一位
name_list.pop()
#pop方法可以指定要删除的索引
name_list.pop(3)
#clear方法默认清空整个列表
name_list.clear()
print(name_list)

#（知道）使用del关键字(delete)删除列表元素
del name_list[2]

#del关键字本质是用来将一个变量从内存中删除的
name="小明"
del name
print(name)
#del不常用
#len(length长度) 函数可以统计列表中元素的总数
list_len = len(name_list)
print("列表中包含%d个元素" % list_len)
#count 方法可以统计列表中某一个数据出现的次数
name_list.count("张三")

#如果列表中有两个重复的元素，remove只会移除第一次出现的元素

#升序
name_list.sort()

#降序
name_list.sort(reverse=True)

#反转
name_list.reverse()