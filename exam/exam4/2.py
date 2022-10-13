def password(login_info):
    judge=False
    keys=''
    while 1:
        user=str(input("输入用户名:"))
        for key in login_info:
            if user==key:
                judge=True
                keys=key
                break
        if judge==True:
            break
        else:
            print("用户名错误")
    new_password=str(input("输入新的密码:"))
    while 1:
        if len(new_password)<8:
            print("密码长度应该不少于8位")
        elif new_password.isdigit()==True:
            print("密码缺少字母")
        elif new_password.isalpha()==True:
            print("密码缺少数字")
        else:
            print("重置成功")
            if len(login_info[login_info.keys(keys)])==3:
                login_info.keys(keys).pop
                login_info.keys(ke
            else:
            break
    '''
    if new_password in value:
        print("请使用未使用过的密码")
    return tuple(temp)
    '''
login_info={'user1':["abc"],
            'user2':["def","hjk","lmn"],
            }
password(login_info)