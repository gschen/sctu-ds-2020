class Stack(object):
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print('空栈不能被弹出')
    def find(self,x):
        return self.stack[x]

s=Stack()
sum=0
for x in ('5','2','C','D','+'):
    if x=='C':
        sum=sum-s.find(-1)
        s.pop()
    elif x=='D':
        a=2*s.find(-1)
        sum=sum+a
        s.push(a)
    elif x=='+':
        b=s.find(-1)+s.find(-2)
        sum=sum+b
        s.push(b)
    else:
        sum=sum+int(x)
        s.push(int(x))
print(sum)