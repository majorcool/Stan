def judge(str_temp):
    if str_temp[::]==str_temp[::-1]:
        print("是回文数")
    else:
        print("不是回文数")
judge("123454321")
