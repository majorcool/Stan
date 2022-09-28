purchasecar=list()
while 1:
    item=str(input("输入商品:"))
    if item=="q":
        break
    purchasecar.append(item)
purchasecar=tuple(purchasecar)
print("商品数量:",len(purchasecar))
for i in range(0,len(purchasecar)):
    print(purchasecar[i])

