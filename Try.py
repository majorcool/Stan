DEL=[1,2,3,4,4]
fish=[1,4,2,4,8,9,9,8,67,3]
for i in DEL:
    fish.pop(fish.index(i))
print(fish)