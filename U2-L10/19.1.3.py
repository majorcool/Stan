def divide(a,b):
    return a/b
try:
    print(divide(20,1))
except ZeroDivisionError:
    Er= Exception("除数为零错误")
    raise Er