class Person:
    def __init__(self, name='df'):
        self.__name = name
    def change(self,name2):
        if len(name2)<10:
            self.__name=name2
            print("New Name %s" % (self.__name))
        else:
            pass
XM=Person()
XM.change('sdfjfwdj')
