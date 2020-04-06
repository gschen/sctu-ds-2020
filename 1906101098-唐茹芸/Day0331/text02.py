#初始化一个类
class Node(object):
    def __init__(self,deta):
        self.data = data
        self.next = None
#初始化一个栈
class Stack(object):
    def __init__(self):
        self.node = Node(None)
        self.head = self.node
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def get_size(self):
        return self.size
    def push(self,data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    def pop(self):
        if not self.is_empty():#判断是否为空
            current_node = self.head.next#保存栈顶元素
            if self.get_size() == 1:
                self.head.next = None
            else:
                self.head.next = self.head.next.next#将头节点指向栈顶的下一个节点
                self.size -=1
                return current_node.data
        else:
            print("栈为空")
    def top(self):
        if not self.is_empty():
            return self.head.next.data
        else:
            print("栈为空")
