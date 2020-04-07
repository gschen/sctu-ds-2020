# 用链表方式实现队列
class Node:
    def __init__(self,val):
        self.val = val
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
    # 添加
    def enqueue(self,val):
        self.size += 1
        que = Node(val)  #创建节点
        if self.head is None:
            self.head = self.end = que
        else:
            self.end.next = que   #将新节点放在尾节点后
            self.end = que   #将尾节点指向新节点
    def dequeue(self,val):
        if self.head is None:
            print('队列为空')
        else:
            self.size -= 1
            self.head = self.head.next
            if self.head is None:
                self.end = None
queue =Queue_()
print(queue.is_empty())