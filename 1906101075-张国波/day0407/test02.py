class Queue:
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
            print('空，不能删')
            return
        else:
            self.size-=1
            self.que.pop(0)


queue=Queue()
queue.enqueue('1')
queue.enqueue('2')
queue.enqueue('3')
print(queue.que_size())