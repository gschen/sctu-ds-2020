class Node:
    def __init__(self,value):
        self.value=value
        self.next=next

class Queue_:
    def __init__(self):
        self.head=None#头节点初始化
        self.end=None#尾节点
        self.size=0

    def is_empty(self):
        if self.size==0:
            return True
        return False

    def que_size(self):
        return self.size

    def enqueue(self,value):
        self.size+=1
        que=Node(value)#创建节点
        if self.head is None:#判断是否存在头节点
            self.head=self.end=que
        else:#如存在
            self.end.next=que#将新节点放在尾巴节点后面
            self.end=que#将尾结点指针指向新节点

    def dequeue(self):
        #判断队列是否为空
        if self.head is None:
            print("empty")
        else:
            self.size-=1
            self.head=self.head.next#删除元素，使头指针指向下一个元素
            if self.head is None:#如果删除元素后，队列没有元素，head，end都应该为None
                self.end=None

queue=Queue_()
queue.enqueue(1)
queue.enqueue(2)

print(queue.is_empty())
queue.dequeue()
queue.dequeue()
print(queue.is_empty())
