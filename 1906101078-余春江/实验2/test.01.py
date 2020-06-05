#L = "Hello,World"
#s = L[::-1]
#print(s)

class Stack:


    #构造函数
    def __init__(self):
        self.data = []


    #压栈
    def push(self,n):
        self.data.append(n)


    #出栈
    def pop(self):
        n = self.data.pop()
        return(n)
    
    
    # 判断栈是否为空
    def is_empty(self):
        return self.data == 0
            
    #计算栈的长度
    def length(self):
        return(len(self.data))
        





s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)

for i in "Hello,World!":
    s.push(i)

# s.pop()
# s.pop()
# s.pop()

while s.is_empty() != True:
    n = s.pop()
    print(n)
















'''
s = "Hello,World"
def func(s):
    l = list(s) #模拟全部入栈
    result = ""
    while len(l)>0:
        result += l.pop() #模拟出栈
    return result
result = func(s)
print(result)
'''