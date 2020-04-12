class Stack(object):
    def __init__(self,limit = 10):#创建空栈
        self.stack = []
        self.limit = limit
    def is_empty(self):#判断是否为空，空则返回true
        return len(self.stack)==0
    def push(self,date):#入栈，使数据成为新的栈顶
        if len(self.stack)>=self.limit:
            print("栈溢出")
        else:
            self.stack.append(date)
    def pop(self):#弹出栈顶，若栈为空，排除异常
        if self.stack:
            return self.stack.pop()
        else:
            print("空栈不能被弹出")
    def top(self):#查看栈顶，若栈为空，排除异常
        if self.stack:
            return self.stack[-1]
    def size(self):#返回栈长度
        return len(self.stack)
stack = Stack()

stack.push(1)
stack.push(3)
stack.push(5)
stack.push(7)
print(stack.size())
print(stack.is_empty())
print(stack.pop())
print(stack.pop())
print(stack.pop())