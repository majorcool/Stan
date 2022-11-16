def sum(matrix):
    count=0
    sum=0
    repeat=[]
    for i in range(0,len(matrix)):
        sum+=matrix[i][count]
        count+=1
    count=len(matrix)-1
    for i in range(len(matrix)-1,-1,-1):
        sum+=matrix[i][count]
        count-=1
    if len(matrix)%2!=0:
        sum-=matrix[(len(matrix)+1)//2-1][(len(matrix)+1)//2-1]

    return sum
print(sum([[1,1,1,1],
                 [1,1,1,1],
                 [1,1,1,1],
                 [1,1,1,1]]
))
