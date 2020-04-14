class Node :
    def __init__(self,value):
        self.value=value
        self.next=next
    


class Queue:
    def __init__(self):
        self.head=None
        self.end=None
        self.size=0
    def is_empty(self):
        if self.size==0:
            return True
        return False
    def que_size(self):
        return self.size

    def enqueue(self,value):
        self.size+=1
        que=Node(value)
        if self.head is None:
            self.head=self.end=que
        else:
            self.end.next=que
            self.end=que
    def dequeue(self):
        if self.head is None:
            print('000')
        else:
            self.size-=1
            self.head=self.head.next
            if self.head is None:
                self.end=None

queue=Queue()
queue.enqueue('a')
queue.enqueue('b')
print(queue.size)
queue.dequeue()
print(queue.size)

    