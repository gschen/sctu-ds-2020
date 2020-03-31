class Stack(object):
    def __init__(self,limit=10):
        self.stack=[]
        self.limit=limit
    #判断栈是否为空
    def is_empty(self):
        return len(self.stack)==0
    #入栈
    def push(self,data):
        if len(self.stack)>=self.limit:
            print('栈溢出')
        else:
            self.stack.append(data)
    #弹出栈顶元素
    def pop(self):
        if self.stack:#如果栈不为空
            return self.stack.pop()
        else:
            print("空栈不能弹出")
    #查看栈顶元素
    def top(self):
        if self.stack:#如果栈不为空
            return self.stack[-1]
    #返回栈的长度
    def size(self):
        return len(self.stack)
        
stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)   
print(stack.size())  
