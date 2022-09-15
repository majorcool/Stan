correct_number=66
guess_number=int(input("请输入一个1-100之间的数字"))
if guess_number==correct_number:
    print("Correct")
elif guess_number>correct_number:
    print("猜大了")
else:
    print("猜小了")