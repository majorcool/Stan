def demo1():
    try:
        return int(input("input an integer: "))
    except ValueError:
        print("not an integer --- demo1")


def demo2():
    try:
        return demo1()
    except ValueError:
        print("not an integer --- demo2")


try:
    print('user input:', demo2())
except ValueError:
    print("not an integer")