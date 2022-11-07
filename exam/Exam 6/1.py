def is_power_of_3_v1(n):
    count=0
    while 1:
        if n%3==0:
            n/=3
            count+=1
        elif n==1 and count>=1:
            return True
        else:
            return False
def is_power_of_3_v2(n):
    temp=3
    for i in range(0,32):
        temp=3**i

        if n==temp:
            return True
    return False
print(is_power_of_3_v2(80))


