#用链表的方式实现队列
class Node:
    #初始化,value为当前节点的值
    def __init__(self, value):
        self.value=value
        self.next=next

class Queue_:
    #初始化队列
    def __init__(self):
        #头节点初始化
        self.head = None
        #尾节点初始化
        self.end = None
        #队列的长度
        self.size = 0

    #判断是否为空
    def is_empty(self):
        if self.size == 0:
            return True
        return False

    #返回队列的长度
    def que_size(self):
        return self.size

    #列表添加元素
    def enqueue(self, value):
        self.size += 1
        #创建节点
        que = Node(value)
        #判断是否存在头节点
        if self.head is None:
            self.head = self.end=que
        #如果存在头节点
        else:
            #将新节点放在尾节点后面
            self.end.next = que
            #将尾节点指针指向新节点
            self.end = que

    #删除队列元素
    def dequeue(self):
            #判断队列是否为空
            if self.head is None:
                print("队列为空！")
            else:
                self.size -= 1
                #删除，头指针指向下一个
                self.head = self.head.next
                #如果队列删除元素后，就没有元素了，head和end此时应该都为None
                if self.head is None:
                    self.end = None


queue=Queue_()
print(queue.is_empty())
queue.enqueue(1)
queue.enqueue(2)
queue.dequeue()
print(queue.que_size())