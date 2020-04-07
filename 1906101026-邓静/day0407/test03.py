#用链表的方式实现
class Node:
    #初始化,value为当前节点的值
    def  __init__(self,value):
        self.value=value
        self.nxet=next

class Queue_:
    #初始化队列
    def __init__(self):
        self.head=None#头结点初始化
        self.end=None#尾节点初始化
    #判断是否为空
    def is_emptyy(self):
        if self.size==0:
            return True
        return False
    #返回队列的长度
    def que_size(self):
        return self.size
    #列表添加元素
    def enqueue(self,value):
        self.size+=1
        que=Node(value)#创建节点
        if self.head is Node:#判断是否为头节点
            self.head=self.end=que
        else:#如果存在头节点
            self.end.next=que#将新节点放在尾节点后面（第一步）
            self.end=que#将为节点指针指向新节点（第二步）

    #删除队列元素
    def dequeue(self):
        #判断队列是否为空
        if self.head is None:
            print('没东西000')
        else:
            self.size-=1
            self.head=self.head.next#删除元素，使指针指向下一个节点
            if self.head is None:
                self.end=None
q=Queue_()
q.enqueue("1")
q.enqueue("2")
q.enqueue("2")
print(q.que_size())




