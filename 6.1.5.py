def sort(str_):
    space=0
    abc=0
    num=0
    extra=0
    for i in range(0,len(str_)):
        if str_[i].isalpha()==True:
            abc+=1
        if str_[i].isspace()==True:
            space+=1
        if str_[i].isdigit()==True:
            num+=1
        if str_[i].isidentifier()==True:
            extra+=1
    temp=("字母:",abc,"空格:",space,"数字:",num,"其他字符:",extra)
    return temp
print(sort("asd67sg,,  ashdn"))
