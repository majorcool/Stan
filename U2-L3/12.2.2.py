class A:
    def __init__(self):
        self.__u = 10
    def __f1(self):
        self.__u += 1
        print(self.__u)

class B(A):
    def f2(self):
        print(self._A__u)
        pass
    def f3(self):
        self._A__f1()
        pass
test=B()
test.f3()
test.f2()