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
            return self.stack[-1]

    def size(self):
        return len(self.stack)
