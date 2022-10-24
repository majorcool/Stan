def Nim(n):
    if (n-1)%4==0 or (n-2)%4==0 or (n-3)%4==0:
        return True
    else:
        return False

print(Nim(7))