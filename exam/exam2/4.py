Hundred=0
Ten=0
GeWeiShu=0
for i in range(100,1000):
    Hundred = i // 100
    Ten = (i - Hundred * 100) // 10
    GeWeiShu = i - Hundred * 100 - Ten * 10
    if Hundred**3+Ten**3+GeWeiShu**3==i:
        print(i)
