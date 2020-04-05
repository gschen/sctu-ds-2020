class stack(object):
    def_ init_ (self,limit=10):
        self . stack=[]
        self .limit=limit
#判断栈是否为空
def is_ empty(sel1f):
    return len(self . stack)==0
#入栈
def push(self,data):
    if len(self . stack)>=self .limit:
        print(栈溢出)
    else:
        self .stack . append( data )
#弹出栈顶元素
def pop( self):
    if self . stack : #如果栈不为空
        return self . stack . pop()
    else:
        print( "空栈不能弹出”)
#查看栈顶元素
def top(self):
    if self. stack : #如果栈不为空
        return self .stack[-1]
#返回栈的长度
def size(self):
    return len(self .stack)


stack=Stack()
stack . push(1)
stack . push(2)
stack. push(3)
print( stack. size())
print(stack. top())
print(stack. pop())
print( stack. top())



class Node(object):
    def_ init_ (self,data):
        self.data = data
        self.data = data
        self.next = None
class stack(object):
    def__init__(self):
        self .node = Node(Node)
        self.head = self .node
        self.size = 0
    def is_ empty(self):
        return self.size == 0
    def get size(self):
        return self. size
    def push(self ,data):
        node = Node(data)
        node.next = self.head .next
        self.head.next = node
        self.size +=1
    def pop(self):
        if not self.is empty(): #判断是否为空
            current node = self.head.next #保存栈顶元素
            if self.get size() == 1:
                self .head.next = Node
                self.size-=1
            else:
                self .head.next = self .head.next.next #头节点指向栈项
                self.size -= 1
                return current node . data
        else:
            print("栈为空")
    def top(self):
        if not self.is empty():
            return self.head.next.data
    else:
        print("栈为空")
s=Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.is_empty())
print(s.top())
s.top()
s.top()
s.top()
print(s.is_empty())
print(s.get_size())
print(s.top())
