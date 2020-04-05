class Node(object):
    def_init_(self,data):
        self.data=data
        self.next=None
class Stack(object):
    def_init_(self):
        self.node=NOde(None)
        self.head=self.None
        self.size=0
    def is_empty(self):
        return self.size==0
    def get_size(self):
        return self.size
    def push(self.size):
        node=Node(data)
        node.next=self.head.next
        self.head.next=node
        self.size += 1
    def pop(self):
        if not self.is_empty():
            current_node=self.head.next
            if self.get_size()==1:
                self.head.next=None
            else:
                self.head.next=self.head.next.next
                self.size-=1
                return current_node.data
        else:
            print("栈为空")
    def top(self):
        if not self.is_empty():
            return self.head.next.data
        else:
            print("栈为空")


