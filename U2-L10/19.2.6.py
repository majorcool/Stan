count=0
def sub(num1,num2):
    global count
    if num1==0 or num2==0:
        return count
    if num1>=num2:
        count += 1
        return sub(num1-num2,num2)

    else:
        count += 1
        return sub(num1,num2-num1)
print(sub(10,8))