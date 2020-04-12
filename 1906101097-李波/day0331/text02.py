# coding=utf-8

class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack(object):
    def __init__(self):
        self.node=Node(None)
        self.head=self.node
        self.size=0
    def is_empty(self): # 判断是否为空
        return self.size==0
    def get_size(self): # 栈的长度
        return self.size
    def push(self,data): # 压栈
        node=Node(data)
        node.next=self.head.next
        self.head.next=node
        self.size+=1
    def pop(self): # 出栈
        if not self.is_empty():
            current_node=self.head.next
            if self.get_size()==1:
                self.head.next=None
                self.size-=1
            else:
                self.head.next=self.head.next.next
                self.size-=1
                return current_node.data
        else:
            print('栈为空')
    def top(self): # 返回栈顶
        if not self.is_empty():
            return self.head.next.data
        else:
            print('栈为空')


s=Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.is_empty())
print(s.top())
s.pop()
print(s.top())
s.pop()
s.pop()
print(s.is_empty())
print(s.top())