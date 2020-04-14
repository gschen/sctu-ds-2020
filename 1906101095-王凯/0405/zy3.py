#用链表的方式实现队列
class Node:
    #初始化,value为当前节点的值
    def __init__(self,value):
            self.value=value
            self.next=next

class Queue_:
    #初始化队列
    def __init__(self):
        self.head=None#头节点初始化
        self.end=None#尾节点初始化
        self.size==0#队列长度
        #判断头节点是否为空
    def is_empty(self):
        if self.size==0:
            return True
        return False
         #返回队列的长度
    def que_size(self):
        return self.size
        #列表添加元素
    def enqueue(self,vaule):
        self.size+=1
        que=Node(vaule)#创建节点
        if self.head is None:#判断头节点是否存在
            self.head=self.end=que
        else:#存在头节点
            self.end.next=que#将新节点放在尾节点后
            self.end=que#将尾节点指针指向新节点

        #删除队列元素
    def dequeue(self):
        #判断队列是否为空
        if self.head is None:
            print('空')
        else:
            self.size-=1
            self.head=self.head.next#删除元素，使头指针指向下一个元素
            if self.head is None:#如果删除元素后队列没有元素，此时head and end均为None
                self.end=None
