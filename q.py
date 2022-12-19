class Queue:
    def __init__(self):
        self.entries=[]
        self.length=0
        self.front=0
    def enqueue(self,item):
        self.entries.append(item)
        self.length+=1
    def quit(self):
        self.length-=1
        dequeued=self.entries[self.front]
        self.front+=1
        self.entries=self[self.front:]
        return dequeued
    def peek(self):
        return self.entries[0]
    def print(self):
        print(self.entries)
        #找到max
        #找到min
    def max(self):
        for i in
l=Queue()
l.enqueue('u')
l.enqueue(12)
l.print()