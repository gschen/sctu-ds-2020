#用链表的方式实现队列
class Node:
    #初始化,vlaue为当前节点的值
    def __init__(self,value):
        self.value = value
        self.next = next

class Queue_:
    #初始化队列
    def __init__(self):
        self.head = None #头节点初始化
        self.end = None #尾节点
        self.size = 0 #队列的长度
    #判断是否为空
    def is_empty(self):
        if self.size == 0:
            return True
        return False

    #返回队列长度
    def que_size(self):
        return self.size
    
    #列表添加元素
    def enqueue(self,value):
        self.size+=1
        que = Node(value)#创建节点
        if self.head is None:#判断是否存在头节点
            self.head = self.end = que
        else:#如果存在头节点
            self.end.next = que #将新节点放在尾节点后面(第一步)
            self.end = que #将尾节点指针指向新节点（第二步）
    
    #删除队列元素
    def dequeue(self):
        #判断队列是否为空
        if self.head is None:
            print("0000000")
            return
        else:
            self.size-=1
            self.head = self.head.next #删除元素，使头指针指向下一个元素
            #如果删除元素后，队列没有元素，head此时为none，end此时也应该为none
            if self.head is None: 
                self.end = None            
queue=Queue_()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.dequeue()
print(queue.is_empty())
print(queue.que_size())
