class Queue_:
    def __init__(self):
        self.que=[]
        self.size=0

    def is_empty(self):
        if self.size==0:
            return True
        return False
    
    def que_size(self):
        print(self.size)

    def enqueue(self,value):
        self.size+=1
        self.que.append(value)
    
    def dequeue(self):
        if self.size==0:
            print("失败")
            return
        else:
            self.size-=1
            self.que.pop(0)


queue=Queue_()
print(queue.is_empty())
queue.que_size()
queue.dequeue()
queue.enqueue(1)
queue.que_size()
print(queue.is_empty())
queue.dequeue()
print(queue.is_empty())
queue.que_size()
    
        