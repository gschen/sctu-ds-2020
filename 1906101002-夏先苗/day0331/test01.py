class Stack(object):#初始化栈
    def __init__(self,limit=10):
        self.stack=[]
        self.limit=limit
    def is_empty(self):#判断是否为空
        return len(self.stack)==0
    def push(self,data):#判断栈是否溢出
        if len(self.stack)>=self.limit:
            print('栈溢出')
        else:
            self.stack.append(data)
    def pop(self):#弹出栈顶元素
        if self.stack:
            return self.stack.pop()
        else:
            print('空栈不能被弹出')
    def top(self):#查看栈顶元素
        if self.stack:
            return self.stack[-1]
    def size(self):#返回站的长度
        return len(self.stack)
stack=Stack()
print(stack.size())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.is_empty())
print(stack.top())
print(stack.top())
print(stack.top())
