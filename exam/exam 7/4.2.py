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
    keeper.perform()
    keeper




