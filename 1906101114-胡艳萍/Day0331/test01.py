class Stack(object):
    # 创建空栈
    def __init__(self,limit=10):
        self.stack=[]
        self.limit=limit
    # 判断栈是否为空，空返回true
    def is_empty(self):
        return len(self.stack)==0
    # 入栈，使elem成为新的栈顶(压栈)
    def push(self,data):
        if len(self.stack)>=self.limit:
            print("栈溢出")
        else:
            self.stack.append(data)
    # 弹出栈顶元素，若栈为空，抛出异常
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("空栈不能被弹出")
    # 查看栈顶，若栈为空，抛出异常
    def top(self):
        if self.stack:
            return self.stack[-1]
    # 返回栈的长度
    def size(self):
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

