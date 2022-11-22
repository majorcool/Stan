# 1. 类方法如何定义？
'''
@classmethod #告诉解释器这是一个方法
def 类方法名(cls): #第一个参数必须是cls,类似self,哪一个类调用的cls,cls就是哪一个类
    pass
#cls.用于调用
'''
class Tool(object):
    count=0
    @classmethod
    def show_tool_count(cls):
        print("工具数量的 %d" % cls.count)
    def __init__(self,name):
        self.name=name
        Tool.count+=1
tool1=Tool("斧头")
tool2=Tool("dd")
Tool.show_tool_count()
# 2. 静态方法如何定义？
'''
如果有一个类封装着一个既不需要访问实例属性或调用实例属性也不需要访问类属性或者调用类方法的方法，那么可以把这个方法封装成一个静态方法
@staticmethod
def 静态方法名():
    pass
'''
class Dog(object):
    @staticmethod
    def run():
        print("小狗要跑")
Dog.run()