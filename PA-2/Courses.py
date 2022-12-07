class Class:
    def __init__(self,name,teacher,score,must,storage):
        self.must=bool(must)
        self.score=score
        self.teacher=teacher
        self.name=name
        self.storage=storage