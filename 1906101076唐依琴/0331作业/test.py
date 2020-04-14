class Stack(object):
    def __init__(self):
        self.stack = []
    def score(self,Date):
        x=list(map(str,list(range(100))))
        for date in Date:
            if date in x:
                self.stack.append(int(date))
            if date=='C':
                self.stack=self.stack[:-1]
            if date=='D':
                self.stack.append((self.stack[-1])*2)
            if date=='+':
                self.stack.append(sum(self.stack[-2:]))
    def result(self):
        return sum(self.stack)
T=Stack()
T.score(["5","2","C","D","+"])
print(T.result()) 
