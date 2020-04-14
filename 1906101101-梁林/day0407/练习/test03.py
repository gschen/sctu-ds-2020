#链表方式实现队列
class Node:
    #初始化
    def __init__(self,value):
        self.value=value
        self.next=next
class Queue_:
    #初始化队列
    def __init__(self):
        self.head=None#头节点初始化
        self.end=None#尾节点初始化
        self.size=0#队列长度

    #判断是否为空
    def is_empty(self):
        if self.size==0:
            return True
        return False

    #返回长度
    def que_size(self):
        return self.size

    #队列添加元素
    def enqueue(self,value):
        self.size+=1
        que=Node(value)#创造节点
        if self.head is None:
            self.head=self.end=que
        else:#存在头节点
            self.end.next=que#新节点放在尾节点后
            self.end=que#将尾节点指针指向新节点

    #删除元素
    def dequeue(self):
        if self.head is None:
            print('asd')
        else:
            self.size+=1
            self.head=self.head.next
            if self.head is None:
                self.end=None
