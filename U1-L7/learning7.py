#公共方法：列表等都可以使用的方法
#len(item) 计算元素个数
#del(item) 删除元素
a=[1,2,3]
del a[1]
print(a)
#max()找到最大的元素
t_str="asdgdgashjbcjhasbchasc"
print(max(t_str))
#min()找到最小的元素
print(min(t_str))
#用max或min查找字典中的元素时，只会查找key
t_dict={"a":"z","b":"y","c":"v"}
print(max(t_dict))
#可以用<>=对变量进行比较，返回True或者False  字典不可以比较
print([1,200,3]<[3,2,1])

#公共方法：切片
print([0,1,2,3,4][1:3])
#{"a":"a","b","b"}[0:1]  字典不支持切片

#列表相加/相乘可以组合成一个列表
print([1]*5)
print([1,2]+[3,4])

#元组也可以
print((1,2)*2)

#print({"a":"a"}*3) 字典不可以乘

#字符串的拼接
print("hello"+"world")

#元组的拼接
print((1,2)+(3,4))

#列表的拼接
print([1,2]+[3,4])

print([1,2].extend([3,4]))
print([1,2].append(6))

#如果给列表append一个列表，这个append的列表是作为一个元素append进去的，并不是合并
t_list=[1,2,3,4]
t_list.append([1,2,3])
print(t_list)

#可以用in来判断一个元素是不是在一个变量中
if 1 in [1,2,3,4]:
    print("in")

#可以用not in 来判断一个元素是不是不在一个变量中
if 1 not in [2,3,4]:
    print(True)

#字典也可以用in来判断,但是只能判断字典的key，不能判断字典的value
print("a" in {"a":"sd"})

#可以在for后面跟else 执行条件为：当for从头到尾执行完，没有被break退出循环后就会执行else里面的代码
for char in [1,2,3,4,5]:
    print(char)
    break#使用了break所以else不会执行
else:
    print("执行else")

students=[
    {"name":"LB"},
    {"name":"L"}
]
find_name="B"
for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"]==find_name:
        print("找到了%s" % find_name)
        break#如果已经找到就退出循环
else:
    print("未找到")
print("循环结束")