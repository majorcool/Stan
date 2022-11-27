def get_user():
    l=str(input())
    l=l.split(",")
    if len(l)!=5:
        print("请输入五个整数")
        five=Exception("FiveError")
        raise five
    for items in l:
        if items.isdigit()==False:
            print("请输入整数")
            e=Exception("IntegerError")
            raise e
    return l
print(get_user())


