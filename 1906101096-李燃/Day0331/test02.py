class Node(object):   #创建一个节点的类
    def __iinit__(self,data):   
        self.data=data
        self.next=None

class Stack(object):  #初始化一个栈
    def __init__(self):
        self.node=Node(None)
        self.head=self.node   #设置一个头节点
        self.size=0

    def is_empty(self):  #判断是否为空
        return self.size==0

    def get_size(self):
        return self.size   #直接得到他的长度

    def push(self,data):
        node=Node(data)
        node.next=self.head.next
        self.head.next=node
        self.size+=1

    def pop(self):
        if not self.is_empty():  #判断不为空时的情况
            cur_node=self.head.next   #保存栈顶元素
            if self.get_size()==1:
                self.head.next=None
                self.size-=1
            else:
                self.head.next=self.head.next.next  #将头结点指向栈顶的下一个节点
                self.size-=1
                return cur_node.data #返回栈顶元素    
        else:
            print('栈为空')

    def top(self):
        if not self.is_empty():
            return self.head.next.data
        else:
            print('栈为空')

        
s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.is_empty())
print(s.top())
s.pop()
s.pop()
s.pop()
s.pop()
print(s.is_empty())
print(s.get_size())
print(s.top())