class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack(object):
    def __init__(self):
        self.node = None(None)
        self.head = self.node
        self.size = 0
    def is_emputy(self):
        return self.size == 0
    def get_size(self):
        return self.get_size
    def push(self,data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    def pop(self):
        if not self.is_emputy():#判断栈是否为空
           current_node = self.head.next#保存栈顶元素
           if self.get_size() == 1:
               self.head.next = None
               self.size-=1
           else:
                self.head.next = self.head.next.next#将头节点指向栈顶的下一个节点
                self.size -= 1
                return current_node.data
        else:
            print("栈为空")
    def top(self):
        if not self.is_emputy():
            return self.head.next.data
        else:
            print("栈为空")

s=Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.is_emputy())
print(s.top())
s.pop()
s.pop()
s.pop()
print(s.is_emputy())
print(s.get_size())
print(s.top())