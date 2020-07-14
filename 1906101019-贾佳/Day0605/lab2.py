#栈
class stack():
    #构造函数
    def __init__(self):
        self.data = []



    #压栈
    def push(self,n):
        self.data.append(n)



    #出栈
    def pop(self):
        n = self.data.pop()
        return n
    
    #判断栈是否为空
    def empty(self):
        return len(self.data)==0
        
    def length(self):
        print(len(self.data))

    
   

    

s = stack()
for i in "Hello,World!":
    s.push(i)

while s.empty() != True:
    n = s.pop() 
    print(n)
    



