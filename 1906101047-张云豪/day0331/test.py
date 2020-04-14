#笔记
class Stack:
    def __init__(self,limit):
        self.stack = []
        self.limit = limit

    def is_empty(self):
        return len(self.stack) == 0

    def push(self,num):
        if len(self.stack) >= self.limit:
            print('溢出')
        else:
            self.stack.append(num)

    def top(self):
        if self.stack:
            return self.stack[-1]

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack2(object):
    def __init__(self):
        self.node=Node(None)
        self.head=self.node
        self.size=0
    def is_empty(self):
        return self.size==0
    def get_size(self):
        return self.size
    def push(self,data):
        node=Node(data)
        node.next=self.head.next
        self.head.next=node
        self.size+=1
    def pop(self):
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
    def top(self):
        if not self.is_empty():
            return self.head.next.data
        else:
            print('栈为空')

s=Stack2()
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




#作业
class Stack(object):
    def __init__(self):
        self.stack = []
    def sum_he(self,Date):
        a=list(map(str,list(range(100))))
        for date in Date:
            if date in a:
                self.stack.append(int(date))
            if date == 'C':
                self.stack = self.stack[:-1]
            if date == 'D':
                self.stack.append((self.stack[-1])*2)
            if date == '+':
                self.stack.append(sum(self.stack[-2:]))
    def result(self):
        return sum(self.stack)
A=Stack()
A.sum_he(["5","2","C","D","+"])
print(A.result())
