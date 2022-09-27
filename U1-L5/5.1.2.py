common_year=[31,28,31,30,31,30,31,31,30,31,30,31]
leap_year=[31,29,31,30,31,30,31,31,30,31,30,31]
count=1
for num in range(0,12):
    print("平年的%d月有%d天,闰年的%d月有%d天" % (count, common_year[num], count, leap_year[num]))
    count+=1