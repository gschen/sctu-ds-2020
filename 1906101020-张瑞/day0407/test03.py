#初始化链表
class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=next
 #用链表的方式实现队列
class Queue_:
    #初始化队列
    def __init__(self):
        self.head=None#初始化头结点
        self.end=None#尾节点初始化
        self.size=0
    def is_empty(self):
        if self.size==0:
            return True
        return False
    #返归队列的长度
    def que_size(self):
        return self.size
    #列表添加元素
    def enqueue(self,value):
        self.size+=1
        que=Node(value)#创建节点
        if self.head is None:#判断是否存在头节点
            self.head=self.end=que
        else:
            self.end.next=que#将新节点放在尾节点后
            self.end=que#将尾节点指针指向新节点
    #删除队列元素
    def dequeue(self):
        if self.head is None:
            print('000')
        else:
            self.size-=1
            self.head=self.head.next#删除元素使头指针指向下一个元素
            if self.head is None:
                self.end=None

queue=Queue_()
queue.enqueue(2)
queue.enqueue(5)
print(queue.que_size())
queue.dequeue()
print(queue.que_size())