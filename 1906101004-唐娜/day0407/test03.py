#用链表的方法实现队列
class Node:
    #初始化,value为当前结点的值
    def __init__(self,value):
        self.value=value
        self.next=next


class Queue_:
    #初始化队列
    def __init__(self):
        self.head=None#头结点初始化
        self.end=None#尾结点初始化
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
    def enqueue(self,value):
        self.size+=1
        que=Node(value)#创建结点
        if self.head is None:#判断是否存在头结点
            self.head=self.end=que
        else:#如果存在头结点
            self.end.next=que#将新结点放在尾结点后面(第一步)
            self.end=que#将尾结点指针指向新结点(第二步)

    #删除队列元素
    def dequeue(self):
        #判断队列是否为空
        if self.head is None:
            print("没东西，不能删")
        else:
            self.size-=1
            self.head=self.head.next#删除元素，使头指针指向下一个元素
            if self.head is None:#如果删除元素后，队列没有元素，head此时为None，end此时也应该为None
                self.end=None
queue=Queue_()
queue.enqueue("a")
queue.enqueue("b")
print(queue.que_size())
queue.dequeue()
print(queue.que_size())