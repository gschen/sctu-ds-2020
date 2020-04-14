# 创建节点类
class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None
# 创建栈的类
class Stack(object):#初始化一个栈
    def __init__(self):
        self.node=Node(None)
        self.head=self.node
        self.size=0
    def is_empty(self):#判断是否为空
        return self.size==0
    def get_size(self):#直接得到长度
        return self.size
    def push(self,data):#堆栈
        node=Node(data)#现在的节点指向栈顶节点
        node.next=self.head.next
        self.head.next=node
        self.size+=1
    def pop(self):
        if  not self.is_empty():#判断是否为空
            current_node=self.head.next#保存栈顶元素
            if self.get_size()==1:
                self.head.next= None#没有下一个节点
            else:
                self.head.next=self.head.next.next#将头节点指向栈顶的下一个节点
                self.size-=1
                return current_node.data
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
print(s.is_empty)
print(s.top())
print(s.top)
s.pop()
s.pop()
s.pop()
print(s.is_empty())



