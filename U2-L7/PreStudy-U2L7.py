'''
1.什么是多态?
不同的子类对象带哦用相同的父类方法，产生不同的执行效果

2.如何实现多态?
class Dog(object):
def __init__(self,name):
self.name=name

def game(self):
print("%s蹦蹦跳跳的玩耍" % self.name)

class Xiaotiandog(Dog)
def game(self):
print("%s 飞到天上去玩耍" % self.name)

class Person(object):
def __init__(self,name):
self.name=name
def game_with_dog(self,dog):
print("%s and %s 快乐的玩耍" % (self.name,dog.name))
dog.game()

#wangcai=Dog("旺财")
wangcai=Xiaotiandog("飞天旺财")

xiaoming=Person("小明")

xiaoming.game_with_dog(wangcai)
'''