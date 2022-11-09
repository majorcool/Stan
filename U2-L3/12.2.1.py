class A:
    def __init__(self):
        self.__a = 1
    def change(self):
        self.__a = 2
        print(self.__a)

class B(A):
    def __init__(self):
        self.__b = 2
    def changea(self):
        super().change()
b=B()
b.changea()