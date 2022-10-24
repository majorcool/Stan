def reverse(n):
    binary=bin(n)
    str_=str(binary)
    str_fin=""
    str_=str_.removeprefix("0b")
    for i in range(0,32-(len(str_))):
        str_fin+='0'
    str_fin+=str_
    str_2=str_fin[::-1]
    print(int(str_2,2))
reverse(43261596)
