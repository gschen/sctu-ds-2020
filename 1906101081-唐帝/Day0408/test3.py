#用链表的方式实现队列
class Node:
    #初始化，value为当前节点的值
    def __init__(self,value):
        self.value=value
        self.next=next

class Queue_:
    #初始化队列
    def __init__(self):
        self.head=Node#头节点初始化
        self.end=None#尾节点初始化
        self.size=0#队列的长度

    #判断队列是否为空
    def is_empty(self):
        if self.size==0:
            return True
        return False
    #返回队列的长度
    def que_size(self):
        return self.size
    #列表添加元素
    def enqeueue(self,value):
        self.size+=1
        que=None(value)#创建节点
        if slef.head is None:#判断是否存在头节点
            self.head=self.end=que
        else:#如果存在头节点
            self.end.next=que#将新节点放在尾节点后面
            self.end=que#将尾节点指针指向新节点

    #删除队列元素
    def dequeue(self):
        #判断队列是否为空
        if self.head is None:
            print('000')
        else:
            self.size-=1
            self.head=self.head.head#删除元素，使头指针指向下一个元素
            if self.head is None:#如果删除后队列没有元素，head此时为None，end此时为None
                self.end=None








