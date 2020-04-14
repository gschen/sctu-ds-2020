class Stack(object):
    def __init__(self,limit=10):    #初始化一个栈
        self.stack=[]
        self.limit=limit   #limit是容量
    def is_empty(self):     #判断是否为空
        return len(self.stack)==0
    def push(self,data):
        if len(self.stack)>=self.limit:
            print("栈溢出")
        else:
            self.stack.append(data)
    def pop(self):
        if self.stack:   #如果有元素，就弹出栈顶
            return self.stack.pop()   #-1是最后一个元素，就是栈顶
        else:
            print('空战不能弹出')
    def top(self):           #查看栈顶元素
        if self.stack:
            return self.stack[-1]
    def size(self):               #返回长度
        return len(self.stack)
    
stack=Stack()
print(stack.size())

stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
print(stack.is_empty())
print(stack.top())
print(stack.pop())