age=0
while(1):
    print("你多大")
    age=int(input())
    if age<3:
        print("免费")
        continue
    if age<=12:
        print("10Dollar")
    else:
        print("15Dollar")