def Taxes(brackets,income):
    Tax=0
    Record=0
    for items in brackets:
        if income>=items[0]:
            income-=(items[0]-Record)
            Tax+=(items[0]-Record)*items[1]*0.01
        elif income>0:
            Tax+=income*items[1]*0.01
            return Tax
        Record=items[0]
    if Tax==0:
        return 0
print(Taxes([[1,0],[4,25],[5,50]], income = 0))