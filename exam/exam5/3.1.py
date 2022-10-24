def pw(user_info):
    judge=[False,False,False]
    oldpw=str(input("输入原密码"))
    newpw=str(input("输入新密码"))
    cornewpw=str(input("确认新密码"))
    if oldpw!=user_info["password"]:
        print("原密码不正确")
        return False
    for char in newpw:
        if char.islower() == True:
            judge[0]=True
        if char.isupper() == True:
            judge[1]=True
        if char.isdigit()==True:
            judge[2]=True
        if char.isdigit()==False and char.isupper()==False and char.islower()==False:
            print("密码中只能包含大小写英文符号与数字")
            return False
    if len(newpw)<8:
        print("密码至少要有八位")
        return False
    if newpw!=cornewpw:
        print("新密码不一致")
        return False
    if judge.count(True)>=2:
        user_info['password']=newpw
    else:
        print("密码中请至少包含英文大小写字母和数字中的两种")
        return False
    print("修改成功")
    return True


pw({'username':'user1',
          'password':'a1234567A'
          })