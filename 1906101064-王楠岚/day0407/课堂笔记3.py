#链表的方式实现队列
class Node:
    #初始化,value位当前节点值
    def __init__(self,value):
        self.value=value
        self.next=next

class Queue_:
    #初始化队列
    def __init__(self):
        self.head=None#头结点初始化
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

    #添加元素
    def enqueue(self,value):
        self.size==1
        que=Node(value)#创建节点
        if self.head is None:#判断是否存在头结点
            self.head=self.end=que
        else:#如果存在头结点
            self.end.next=que#将新节点放在尾节点后面1
            self.end=que#将尾节点指针指向新节点2

    #删除元素
    def dequeue(self):
        #判读对可是否为空
        if self.head is None:
            print('队列为空')
        else:
            self.size-=1
            self.head=self.head.next#删除元素使头指针指向下一个元素
            #如果删除元素后队列没有元素head 此时为none,end也该为None
            if self.head is None:
                self.end=None


queue=Queue_()
print(queue.is_empty())
queue.enqueue(1)
print(queue.que_size())