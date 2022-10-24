xiaoming={
"name":"小明",
"age":18,
"gender":True,
"height":1.75#key必须是唯一的，只能用key访问value,不能用value访问key
}#键必须是唯一的
print(xiaoming)#字典输出时顺序是随机的
#取值
print(xiaoming["name"])#在中括号里输入key来取值
#增加/改删
xiaoming["gg"]=18#key不存在就增加
xiaoming["age"]=9#key存在就修改
#删除
xiaoming.pop("name")#选中key就可以删除
print(xiaoming)

#统计键值对数量
print(len(xiaoming))
#合并字典
temp_dict={"a":88}
xiaoming.update(temp_dict)#合并时相同的key会产生覆盖
#清空字典
xiaoming.clear()
#遍历字典
#变量k是每一次循环中，获得的键值对应的key
for k in xiaoming:
    print("%s - %s" % (k,xiaoming[k]))
card_list=[
    {"name":"张三",
     "qq":"12345"},
    {"name":"里斯","qq":"12345"
     }
]
xiaoming={
    "name":"小明",
    "age":12
}
for card_info in xiaoming:
    print(card_info)
