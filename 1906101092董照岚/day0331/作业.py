class Stack(object):
    def __init__(self):
        self.stack = []
        
    def push(self,Date):
        a=list(map(str,list(range(10))))
        for date in Date:
            if date[0] in a:
                self.stack.append(int(date))
            elif date=='C':
                self.stack=self.stack[:-1]
            elif date=='D':
                self.stack.append((self.stack[-1])*2)
            elif date=='+':
                self.stack.append(sum(self.stack[-2:]))
    def result(self):
        return sum(self.stack)
        
A=Stack()
A.push(["5","2","C","D","+"])
print(A.result())
