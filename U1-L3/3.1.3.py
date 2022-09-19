rmb=200000000
month=0
while rmb>=10:
    rmb=rmb/2
    month+=1
print("还剩 %.2f元 用了%d月" % (rmb,month))