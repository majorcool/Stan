def best_profit(price):
    rev=sorted(price,reverse=True)
    if price==rev:
        return 0
    biggest=0
    small=sorted(price)
    big=sorted(price,reverse=True)
    for item in big:
        for items in small:
            if price.index(item)>price.index(items) and (item-items)>biggest:
                biggest=(item-items)
    return biggest

print(best_profit([7,1,5,3,6,4]))