# coding=utf-8

# 栈的创建

class Stack(object):
    def __init__(self,limit=10):
        self.stack=[]
        self.limit=limit
    def is_empty(self): # 判断是否为空
        return len(self.stack)==0
    def push(self,data): # 压栈
        if len(self.stack)>=self.limit:
            print('栈溢出')
        else:
            self.stack.append(data)
    def pop(self): # 弹出栈顶
        if self.stack:
            return self.stack.pop()
        else:
            print('空栈不能被弹出')
    def top(self): # 返回栈顶
        if self.stack:
            return self.stack[-1]
    def size(self): # 栈的长度
        return len(self.stack)
    def print_stack(self): # 打印栈
        print(self.stack)


stack=Stack()
# print(stack.size())

# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# print(stack.size())
# print(stack.is_empty())
# print(stack.top())
# stack.print_stack()
# print(stack.pop())
# print(stack.top())
# stack.print_stack()