def stage(x):
    if x==1:
        return 1
    else:
        return x*stage(x-1)
print(stage(3))