users=('root','user1','user2')
passwords=('123','abc','@*#')
i=0
count=0
count2=0
Break=False
p=0
count3=0
count4=0
while 1:
    user=str(input("用户名:"))
    password=str(input("密码:"))
    count=0
    count2=0
    count3=0
    count4=0
    for i in range(0,3):
        if user==users[i] and password==passwords[i]:
            print("登陆成功")
            Break=True
            break
        if user!=users[p] and user!=users[p+1] and user!=users[p+2] and count!=1:
            print("用户名错误")
            count=1
        if password!=passwords[p] and password!=passwords[p+1] and password!=passwords[p+2] and count2!=1:
            print("密码错误")
            count2+=1
        elif count4!=1 and count!=1 and count2!=1:
            print("用户名密码对不上")
            count4=1

    count3+=1
    if Break==True:
        break
    if count3==3:
        print("错误过多，请晚点尝试")
        break