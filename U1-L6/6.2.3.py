def binary(a,b):
    sum=int(a,2)+int(b,2)
    sum=bin(sum)
    sum=str(sum)
    print(sum[2::])
binary('1010','1011')