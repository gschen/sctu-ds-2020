#栈
class Stack:
    '''
    self .data - 类的成员变量
    self ,data() - 类的函数
    '''
    #构造函数
    def __init__ (self):
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
    #计算栈的长度
    def length(self):
        return len(self.data)  

s = Stack( )
# s. push(1)
# s. push(2)
# s. push(3)

# for i in "Hello,world!":
#     s.push(i)
# while s.empty() != True:
#     n = s.pop()
#     print(n,end="")




stack = []
left = ['{','[','(']
right = ['}',']',')']
#判断给定的字符串是否括号匹配
def match(s):
    for i in s:
        #如果i是左括号，压栈
        if i in left:
            stack. append(i)
        #如果i是右括号，出栈
        if i in right:
            if len(stack)==0:
                return False
            j = stack.pop()# i是右括号， j是左括号

            #判断当前的右括号与出栈的左括号是否匹配*****
            if right.index(i) != left.index(j):
                return False
    # ((())
    if Len(stack) != 0:
        return False
    return True
print(match(')(({))'))






