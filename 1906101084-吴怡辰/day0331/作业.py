class Stack:
    def calPoints(self, ops):
        stack=[]
        for i in ops:
            if i == 'C':
                stack.pop()
            elif i == 'D':
                stack.append(stack[-1]*2)
            elif i == '+':
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(i))
        return(sum(stack))
s = Stack()
print(s.calPoints(["5","2","C","D","+"]))
