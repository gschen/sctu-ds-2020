class Queue:
    #初始化队列
    def __init__(self):
        self.que=[]
        self.size=0 #列表的长度

    #判断队列是否为空
    def is_empty(self):
        if self.size==0:
            return True
        return False

    #返回队列的长度
    def que_size(self):
        return self.size

    #列表添加元素：
    def enqueue(self,value):
        self.size+=1
        self.que.append(value)
    
    #删除队列中的元素：
    def dequeue(self):
        if self.size==0:
            print('队列为空，不能删除')
            return
        else:
            self.size-=1
            self.que.pop(0)

queue=Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.is_empty())
queue.dequeue()
print(queue.is_empty())
print(queue.que_size())

#用链表的方式实现队列：
class Node:
    #初始化,value为当前节点的值
    def __init__(self,value):
        self.value=value
        self.next=next

class Queue_:
    #初始化队列
    def __init__(self):
        self.head=None #头节点初始化
        self.end=None  #尾节点初始化
        self.size==0 #初始化长度
    
    #判断是否为空：
    def is_empty(self):
        if self.size==0:
            return True
        return False
    
     #返回队列的长度
    def que_size(self):
        return self.size

    #列表添加元素：
    def enqueue(self,value):
        self.size+=1
        que=Node(value)#创建节点
        if self.head is None:#判断是否存在头节点
            self.head=self.end=que
        else: #如果存在头节点
            self.end.next=que #将新节点放在尾节点后面(第一步)
            self.end=que #将尾节点指针指向新节点(第二步)
    
    #删除队列中的元素：
    def dequeue(self):
        if self.head is None: #判断队列是否为空
            print('队列为空')
        else:
            self.size-=1
            self.head=self.head.next #删除元素使头指针指向下一个元素
            if self.head is None: #如果删除元素后，队列没有元素,head此时为None,end此时也为None
                self.end=None

queue=Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.is_empty())
queue.dequeue()
print(queue.is_empty())
print(queue.que_size())