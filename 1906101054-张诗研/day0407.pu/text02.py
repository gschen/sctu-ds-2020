class Queue:
    #初始化队列
    def __init__(self):
        self.que=[]
        self.size=0

    def is_empty(self):
        if self.size==0:
            return True
        return False

    def que_size(self):
        return self.size

    def enqueue(self,value):
        self.size+=1
        self.que.append(value)

    def dequeue(self):
        if self.size==0:
            print("empty")
            return
        else:
            self.size-=1
            self.que.pop(0)

queue=Queue()
queue.enqueue(1)
queue.enqueue(2)
<<<<<<< HEAD
print(queue.is_empty())
=======
queue.enqueue(3)
print(queue.is_empty())

>>>>>>> 42f7e6696cd46b332b07cf06f9f1dddc2e18ce48
