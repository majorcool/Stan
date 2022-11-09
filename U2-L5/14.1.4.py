class A:
    def test(self):
        print(1)


class B(A):
    def test(self):
        print(2)
    def upp(self):
        super().test()


class C(B):
    def up(self):
        super().upp()
c=C()
c.up()