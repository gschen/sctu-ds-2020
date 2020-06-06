#栈
class Stack:

    '''
    self.data  - 类的成员变量
    self.data()   - 类的函数
    '''

    #构造函数
    def __init__(self):
        self.data=[]

        #压栈
    def push(self,n):
        self.data.append(n)


    #出栈
    def pop(self):
        n=self.data.pop()
        #print(n)
        return n

#判断栈是否为空
    def cmpty(self):
        return len(self.data)==0


#计算栈的长度
    def length(self):
        return len(self.data)


s=Stack()
# s.push(1)
# s.push(2)
# s.push(3)

for i in 'hello word!':
    s.push(i)
    
# s.pop()
# s.pop()
# s.pop()

while s.empty != True:
    print(s.pop())



