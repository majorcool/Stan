age=int(input())
if age<=0:
    print("请输入正确的年龄")
elif age<1:
    print("鉴定为婴儿")
elif age<=2:
    print("鉴定为幼儿")
elif age<=12:
    print("鉴定为儿童")
elif age>=18 and age<=20:
    print("鉴定为青春期的年轻人的成年人")
elif age>20 and age<=24:
    print("鉴定为属于年轻人的成年人")
elif age>=13 and age<15:
    print("鉴定为青春期的非年轻人")
elif age>=15 and age<=20:
    print("鉴定为青春期的年轻人")
elif age>20 and age<=24:
    print("鉴定为过了青春期的年轻人")
elif age<=64:
    print("鉴定为成年人")
elif age>120:
    print("请输入正确的年龄")
else:
    print("鉴定为老年人")
