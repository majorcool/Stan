# 1. 什么是异常？
'''
如果python解释器遇到一个错误，就会停止程序的运行，并且提示一些错误信息，这就是异常
程序停止运行并提示错误信息这个动作叫做'抛出异常'
'''

# 2. 异常有哪些类型？（如何找到全部的异常类型？)
'''
python报错最后一行的第一个单词就是错误类型
可以把那个单词复制到except后面就能在报错时产生相应的反应
比如
except ZeroDivisionError:
    print("除零错误")
'''
# 3. 如何捕获异常？
'''
在程序开发中，如果对某些代码不能确定是否正确，可以增加try()来捕获异常
如果遇到不同类型的错误，就需要针对不同类型来做出不同的响应
'''
'''
try:
    num=int(input("输入整数"))
except:
    print("请输入正确的整数")
print("-"*50)
'''
'''
num=int(input("?"))
result=8/num
print(result)
'''
'''
try:
    pass
except 错误类型1:
    pass
except (错误类型2，错误类型3）:
    pass
except 错误类型3
    pass
'''
'''
捕获未知错误
语法:
except: Exception as result   #这里result 就是一个变量名，代指错误
   print("产生%d错误" % result)
'''
try: #先执行
    pass
except:#有错误才执行
    pass
else:#try后执行（没错误的前提）
    pass
finally:#无论如何都执行
    pass
# 4. 如何抛出异常？
'''
我们可以根据应用程序特有的业务需求主动抛出异常
1.创建一个Exception异常类
2.使用raise关键字抛出异常对象
'''
def input_password():
    #1.提示用户输入密码
    pwd = input("?")
    #2.判断密码长度>=8,返回用户输入的密码
    if len(pwd)>=8:
        return pwd
    #3.如果<8主动抛出异常
    print("主动抛出异常")
    #1>创建异常对象
    ex = Exception("密码长度不够") #括号里面是错误提示信息
    #2>主动抛出异常
    raise ex
print(input_password())
# 5. 什么是异常的传递？
'''
异常的传递-当函数/方法执行出现异常，会将一场传递给函数/方法的调用一方
如果传递到主程序，仍然没有异常处理，才会终止程序
'''
'''
def demo1():
    return int(input())
def demo2():
    return demo1()
#利用异常的传递性，在主程序中捕获异常
try:
    print(demo2())
except Exception as result:
    print("位置错误 %s" % result)
'''