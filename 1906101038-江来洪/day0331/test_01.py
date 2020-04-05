class Stack(object):
    def __init__(self,limit = 10):
        self.stack = []
        self.limit = limit
    def is_empty(self):
        return len(self.stack) == 0
    def push(self,date):
        if len(self.stack) >= self.limit:
            print('栈溢出')
        else:
            self.stack.append(date)
    def pop(self):
        if self.stack:
            return self.stack.pop() 
        else:
            print('空栈不能被弹出') 
    def top(self):
        if self.stack:
            return self.stack[-1]
    def size(self):
        if self.stack:
            return len(self.stack)
stack = Stack()
print(stack.size())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.size())
print(stack.is_empty())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

