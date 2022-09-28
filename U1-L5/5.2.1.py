menu=("面","土豆","青菜","牛肉","鸡")
for i in range(0,5):
    print(menu[i])
#TypeError: 'tuple' object does not support item assignment
#menu[0]="饭"
new_menu=("面","萝卜","青菜","牛排","鸡")
menu=new_menu
for i in range(0,5):
    print(menu[i])