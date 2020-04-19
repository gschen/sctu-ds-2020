class stack(object):
    def __inint__(self,limit=10):
        self.stack=[]
        self.limit=limit
    def is_empty(self):
        return len(self.stack)==0
    def push(self,data):
        if len(sekf.stack)>=self.limit:
            print("溢出")
        else:
            self.stack.append(data)
    def pop(self):
        if self.stack:
            return self.stacj.pop
        else:
            print("空栈不能弹出")
    def top(self):
        if self.stack:
            return self.stack[-1]
    def size(self):
        return len(self.stack)
    


class node(object):
    def __init__(self,data):
        self.data=data
        self.next=None
class stack(object):
    def __init__(self):
        self.node=node(None)
        self.head=self.node
        self.size=0
    def is_empty(self):
        return self.size==0
    def get_size(self):
        return self.size
    def push(self,data):
        node = node(data)
        node.next=self.head.next
        self.head.next=node
        self.size+=1
    def pop(self):
        if not self.is_empty():#判断是否为空
            current_node=self.head.next#保存栈顶元素
            if self.get_size()==1:
                self.head.next=None
            else:
                self.head.next=self.head.next#将头结点指向栈顶的下一个节点
                self.size-=1
                return current_node.data
        else:
            print("栈为空")
    def top(self):
        if not self.is_empty():
            return self.head.next.data
        else:
            print("栈为空")
           
            