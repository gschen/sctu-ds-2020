class stack(object):
    def __init__(self,limit = 10):
        self.stack = []
        self.limit = limit

    def is_empty(self):
        return len(self.stack) == 0
    def push(self,data):
        if len(self.stack)>=self.limit:
            print("栈溢出")
        else:
            self.stack.append(data)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print('空栈无法弹出')

    def top(self):
        if self.stack:
            return slef.stack[-1]

    def size(self):
        return len(self.stack)



class Node(object):
    def __init__(self,date):
        self.date=date
        self.next=Node
class Stack(object):
    def __init__(self):
        self.node=Node(Node)
        self.head=self.node
        self.size=0
    def is_empty(self):
        return self.size==0
    def get_size(self):
        return self.size
    def push(self,date):
        node=Node(date)
        node.next=self.head.next
        self.head.next=node
        self.size+=1
    def pop(self):
        if not self.is_empty():
            current_node=self.head.next
            if self.get_size()==1:
                self.head.next=Node
                self.size-=1
            else:
                self.head.next=self.head.next.next
                self.size=-1
                return current_node.date
        else:
            print("栈为空")
    def top(self):
         if not self.is_empty():
             return self.head.next.date
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

class Node(object):
    def __init__(self,date):
        self.date=date
        self.next=Node
class Stack(object):
    def __init__(self):
        self.node=Node(Node)
        self.head=self.node
        self.size=0
    def is_empty(self):
        return self.size==0
    def get_size(self):
        return self.size
    def push(self,date):
        node=Node(date)
        node.next=self.head.next
        self.head.next=node
        self.size+=1
    def pop(self):
        if not self.is_empty():
            current_node=self.head.next
            if self.get_size()==1:
                self.head.next=Node
                self.size-=1
            else:
                self.head.next=self.head.next.next
                self.size=-1
                return current_node.date
        else:
            print("栈为空")
    def top(self):
         if not self.is_empty():
             return self.head.next.date
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