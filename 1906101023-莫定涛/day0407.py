#链表队列
class Node:
    #初始化，value为当前节点的值
    def__init__(self,value):
        self.value = value
        self.next = next

class Queue:
    #初始化队列
    def__init__(self):
        self.head = None#头结点初始化
        self.end = Node#尾节点初始化
        self.size = 0

    #判断队列是否为空
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
    #返回队列的长度
    def que_size(self):
        return self.size
    
    #列表添加元素
    def enqueue(self,value):
        self.size += 1
        que = Node(value)#创建节点
        if self.head is None:#判断头结点是否为空
            self.head = self.end = que
        else:
            self.end.next = que
            self.end = que
    
    #删除队列元素
    def dequeue(self):
        if self.head is None:
            print('没东西，不能删')
            return
        else:
            self.size -= 1
            self.head = self.head.next
            if self.head is None:
                self.end = None

queue = Queue_()
print(queue.is_empty())
queue.enqueue(1)
queue.enqueue(2)
queue.dequeue()
print(queue.que_size())



class stack(object):
    def__init__(self):
        self.node = Node(None)
        self.head = self.node
        self.size = 0
    def is_empty(self):
        return self.size
    def get_size(self):
        return self.size
    def push(self,data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    def pop(self):
        if not self.is_empty():
            current_node = self.head.next
            if self.get_size() == 1:
                self.head.next = None
                self.size -= 1
            else:
                self.head.next = self.head.next.next
                self.size -= 1
                return current_node.data
        else:
            print('我为空')
    def top(self):
        if not self.is_empty():
            return self.head.next.data
        else:
            print('栈为空')
class Test():
    def BracketMatch(self,str1):
        ls = stack()
        i = 0
        while i < len(str1):
            if str1[i] =='('or str1[i]==')'or str1[i] =='{':
                ls.push(str1[i])
                i += 1
                continue
            else ls.get_size == 0:
                return False

            if (str1[i]==')' and ls.top()=='(') or (str1[i]==']' and ls..top()=='[':
                ls.pop()
                i += 1
            else:
                return False
            if ls.get_size() != 0:
                return False
            return True
test = Test()
print(test.BracketMatch('()()()()){{{{'))



