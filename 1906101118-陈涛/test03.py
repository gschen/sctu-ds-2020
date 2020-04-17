#链表的方式实现队列
class Node:
    #初始化，value为当前节点的值
    def __init__(self,value):
        self.value = value
        self.next = next

class Queue_:
    def __init__(self):
        self.head = None
        self.end = None
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def que_size(self):
        return self.size
    #列表添加元素
    def enqueue(self,value):
        self.size += 1
        que = Node(value)#创建节点
        if self.head is None:#判断是否存在头节点
            self.head = self.end = que
        else:
            self.end.next = que
            self.end = que
    #删除队列元素
    def dequeue(self):
        #判断队列是否为空
        if self.head is None:
            print('Nothing')
        else:
            self.size -= 1
            self.head = self.head.next
            if self.head is None:
                self.end = None
