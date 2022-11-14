'''1.1:12
1.2:4
1.3:报错
1.4:1
1.5:0110
1.6:A是B的父类,B是A的子类,C是A的子类的子类,D与C都是B的子类
1.7.3个内置方法,1个实例方法.
2个必选参数,1个可选参数
错误:task后面的study,self.talent,self.effort,self.learning_tool,tools.items
2.1.1:没必要这么写,filter_index=results就行了
2.1.2:字典默认遍历的就是key
2.2.3:def __bool__:return True  def __len__:return 0  print(bool(len()))
'''
count=0
def gcd_pro_max_1(n):
    n.sort(reverse=True)
    count=-1
    while max(n)!=min(n):
        count+=1
        for o in range(0,len(n)-1):
           a=o+1
           if n[o]%n[a]==0:
               n[o]=n[a]
           else:
               n[o]=n[o]%n[a]
        if count>=994:
            print("1")
            return False
    print(max(n))

'''
def gcd_pro_max_2(n):
    global count
    if n[count] < n[count+1]:
        n[count], n[count+1] = n[count+1], n[count]

    if n[count+1] == 0:
        return n[count]
    else:
        return gcd_pro_max_2(n[count+1])
gcd_pro_max_2([1,2,3,4,5])
'''
class Animal():
    def __init__(self):
        self.health=100
class Manager(Animal):
    def perform(self):
        self.health-=20
    def __inspect(self,worker):
        self.worker=worker
        self.worker.performance=100
    def feed(self,):
        self.health+=20
class Keeper(Manager):
    def __init__(self):
        super().__init__()
        self.performance=100
        if self.health<80:
            self.performance-=20
    def perform(self):
        return False
class Trainer(Manager):
    def __init__(self):
        super().__init__()
        self.performance=100
    def feed(self):
        return False
def everyday():
    keeper=Keeper()
    trainer=Trainer()
    keeper.feed()
    trainer.perform()
    manager=Manager()
    manager._Manager__inspect(keeper)
    manager._Manager__inspect(trainer)




