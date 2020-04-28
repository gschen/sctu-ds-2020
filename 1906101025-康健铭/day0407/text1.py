class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack(object):
    def __init__(self):
        self.node = Node(None)
        self.head = self.node
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def push(self, data):
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
            print("栈为空！")

    def top(self):
        if not self.is_empty():
            return self.head.next.data
        else:
            print("栈为空！")


class Test():
    def BracketMatch(self, str1):
        ls = Stack()
        i = 0
        while i < len(str1):
            if str1[i] == "(" or str1[i] == "[" or str1[i] == "{":
                ls.push(str1[i])
                i += 1
                continue
            elif ls.get_size == 0:
                return False
            if (str1[i] == ")" and ls.top() == "(") or (str1[i] =="[") or (str1[i] == "}" and ls.top() == "{"):
                ls.pop()
                i += 1
            else:
                return False
        if ls.get_size() != 0:
            return False
        return True



test = Test()
print(test.BracketMatch("()()()((())){{{{"))
        

class Queue:
    #初始化队列
    def __init__(self):
        self.que=[]
        #列表的长度
        self.size=0
      
    #判断队列是否为空
    def is_empty(self):
        if self.size == 0:
            return True
        return False

    #返回队列的长度
    def que_size(self):
        return self.size

    #列表添加元素
    def enqueue(self,value):
        self.size += 1
        self.que.append(value)

    #删除队列元素
    def dequeue(self):
        if self.size == 0:
            print("啥都没有，不能删！")
            return
        else:
            self.size -= 1
            self.que.pop(0)


queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
print(queue.que_size())



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
