class Stack(object):
#创建空栈
def __init__(self,limit=10):
    self.Stack=[]
    self.limit=limit
# 判断是否为空
def is_empty(self):
    return len(self.stack)==0
#堆栈
def push(self,data):
    if len(self.stack)>=self.limit:
        print('栈溢出')
    else:
        self.stack.append(data)
#删除栈顶元素并弹出
def pop(self):
    if self.stack:
        return self.stack.pop()
    else:
        print('空栈不能被弹出')
#查看栈顶元素
def top(self):
    if self.stack:
        renturn self.stack[-1]#栈顶
def size(self):
    return len(sel.stack)
stack=Stack()
stack.push(1)
stack.push(3)