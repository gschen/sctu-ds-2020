class Stack(object):
    #初始化栈
    def __init__(self,limit = 10):
        self.stack = []
        self.limit = limit
    #判断栈是否为空
    def is_empty(self):
        return len(self.stack) == 0
    #入栈
    def push(self,date):
        if len(self.stack)>=self.limit:
            print('栈溢出')
        else:
            self.stack.append(date)
    #弹出栈顶
    def pop(self):
        if self.stack:
            return self.stack[-1]
        else:
            print('空栈')
    #查看栈顶
    def top(self):
        if self.stack:
            return self.stack[-1]
    def size(self):
        return len(self.stack)
    
    
stack = Stack()
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