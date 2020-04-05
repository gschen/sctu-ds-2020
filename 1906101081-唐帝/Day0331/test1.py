class Stack(object):
    def __init__(self,limit=10):#创建空栈
        self.stack=[]
        self.limit=limit
    def is_empty(self):#判断栈是否为空，空返回true
        return len(self.stack)==0
    def push(self,data):#入栈，使数据成为新的栈顶
        if len(self.stack)>=self.limit:
            print('栈溢出')
        else:
            self.stack.append(data)
    def pop(self):#弹出栈顶，若栈为空，抛出异常
        if self.stack:
            return self.stack.pop()
    def top(self):#查看栈顶，若栈为空，抛出异常
        if self.stack:
            return self.stack[-1]
    def size(self):#返回栈的长度
        return len(self.stack)
stack=Stack()
print(stack.size())

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.size())
print(stack.is_empty())
print(stack.top())
print(stack.pop())
print(stack.top())
