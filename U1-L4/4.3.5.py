'''def LX(h):
    Odd = True
    if h % 2 == 0:
        print("行数必须是奇数!!!")
        Odd = False

    if Odd == True:
        for i in range(1, h // 2 + 2):
            return(print(" " * (h - i), end=""),print("*" * (2 * i - 1)))
        for i in range(h // 2, 0, -1):
            return(print(" " * (h - i), end=""),print("*" * (2 * i - 1)))
print(LX(5))
'''
#太难不会