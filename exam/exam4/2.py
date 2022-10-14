def password(login_info):
    judge=False
    keys=''
    count=0
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
    while 1:
        new_password = str(input("输入新的密码:"))
        if len(new_password)<8:
            print("密码长度应该不少于8位")
        elif new_password.isdigit()==True:
            print("密码缺少字母")
        elif new_password.isalpha()==True:
            print("密码缺少数字")
        else:
            for pass_word in login_info[user]:
                if new_password==pass_word:
                    print("请设置未使用过的密码")
                    continue
                count+=1
            if count<=2:
                login_info[user].append(new_password)
                print("已重置密码")
                break
            else:
                login_info[user].pop()
                login_info[user].append(new_password)
                print("已重置密码")
                break
    temp_tuple=[user,]
    for psw in login_info[user]:
        temp_tuple.append(psw)
    return tuple(temp_tuple)

login_info={'user1':["abc"],
            'user2':["def","hjk","lmn"],
            }
print(password(login_info))