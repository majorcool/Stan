def fi():
    try:
        return int(input())
    finally:
        print("打印了finally")
print(fi())
'''
首先finally的运行不受try或者except影响
finally的运行始终在return前
如果有except那就会先运行except
就算报错,finally也会在报错前运行
'''