Tired=False
Day=5 #1代表周几 比如7就是周日
Hungry=False
willing_to_learn=True
if Day==1 or Day==2 or Day==3 or Day==4 or Day==5:
    if Tired==False:
        if Hungry==False:
            if willing_to_learn==True:
                print("去学习")
            else:
                print("不想学")
        else:
            print("去吃饭")
    else:
        print("补个觉")
else:
    print("休息日不想学")