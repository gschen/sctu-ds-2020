#链表的方式实现队列
class Node(object):
    #初始化，value为当前结点的值
    def __init__(self,value):
        self.value = value
        self.next = next
class Queue(object):
    #初始化队列
    def __init__(self):
        self.head = None#头节点初始化
        self.end = None#尾节点初始化
        self.size = 0#队列的长度
    #判断是否为空
    def is_empty(self):
        return self.size == 0
    #返回队列长度
    def que_size(self):
        return self.size
    #列表添加元素
    def enqueue(self,value):
        self.size += 1
        que = Node(value)#创建节点
        if self.head == None:#判断是否存在头节点
            self.head=self.end = que
        else:#如果存在头节点
            self.end.next = que#将新节点放到尾结点后面（第一步）
            self.end = que#将尾结点指针指向新节点（第二步）
    #删除队列节点
    def depueue(self):
        #判断队列是否为空
        if self.head == None:
            return "队列为空"
        else:
            self.size -= 1
            self.head = self.head.next#删除元素，使头指针指向下一个元素
            if self.head == None:#如果删除元素后队列为空了
                self.end = None#尾结点此时为None
queue = Queue()
print(queue.size)
print(queue.is_empty())
queue.enqueue(1)
queue.enqueue(2)
print(queue.is_empty())
print(queue.depueue())
print(queue.depueue())
print(queue.size)

