#初始化一个栈
class Stack(object):
    def __init__(self,limit=10):
        self.Stack=[]
        self.limit=limit
    #判断栈是否为空：
    def is_empty(self):
        return len(self.Stack)==0
    #判断栈是否满了
    def push(self,data):
        if len(self.Stack)>=self.limit:
            print('栈溢出')
        else:
            self.Stack.append(data)
    def pop(self):
        if self.Stack:
            return self.Stack.pop()
        else:
            print('空栈不能被弹出')
    #查看栈顶的元素
    def top(self):
        if self.Stack:
            return self.Stack[-1]#-1为栈顶
    def size(self):
        return len(self.Stack)

a=Stack()
a.push(1)
a.push(2)
print(a.size())
print(a.is_empty())
print(a.top())

class Node(object):
    def __init__(self,data):  #创建节点的类
        self.data=data
        self.next=None
class Stack(object):  #初始化栈
    def __init__(self):
        self.node=Node(None)
        self.head=self.node
        self.size=0
    def is_empty(self):
        return self.size==0
    def get_size(self):
        return self.size
    def push(self,data):  #压栈
        node=Node(data)   #创建一个节点
        node.next=self.head.next  #将头节点加进来
        self.head.next=node    
        self.size+=1
    def pop(self):
        if not self.is_empty():   #判断是否为空
            current_node=self.head.next   #保存栈顶元素
            if self.get_size()==1:
                self.head.next=None
                self.size-=1
            else:
                self.head.next=self.head.next.next  #将头节点指向栈顶的下一个节点
                self.size-=1
                return current_node.data    #返回刚刚保存栈顶的元素
        else:
            print("栈为空")
    def top(self):   #返回栈顶元素
        if not self.is_empty():
            return self.head.next.data
        else:
            print("栈为空")

s=Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.is_empty())
print(s.top())
s.pop()
s.pop()
s.pop()
print(s.is_empty())
print(s.get_size())
print(s.top())
