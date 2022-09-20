odd = 0
even = 0
sum = 0
i = 1
PanDing = 0
while i < 101:
    sum = sum + i
    PanDing = i % 2
    if PanDing == 0:
        even = even + i
    else:
        odd = odd + i
    i = i + 1
print(sum)
print(odd)
print(even)

