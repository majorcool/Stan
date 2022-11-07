'''
继承实现代码的重用，相同的代码不需要重复的编写
'''
class Animal:
    def eat(self):
        print('吃')
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")
#创建一个对象-狗对象
#继承的概念-子类拥有父类所有的方法和属性
class Dog(Animal):
    def bark(self):
        print("汪汪叫")
'''子类父类
派生类 基类
继承 派生
继承有传递性
'''
class Cat(Animal):
    def catch(self):
        print("抓老鼠")
