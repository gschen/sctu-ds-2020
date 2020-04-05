class Stack(object):
    def __init__(self):
        self.stack = []
    def sum_he(self,Date):
        a=list(map(str,list(range(100))))
        for date in Date:
            if date in a:
                self.stack.append(int(date))
            if date=='C':
                self.stack=self.stack[:-1]
            if date=='D':
                self.stack.append((self.stack[-1])*2)
            if date=='+':
                self.stack.append(sum(self.stack[-2:]))
    def result(self):
        return sum(self.stack)
A=Stack()
A.sum_he(["3","2","C","D","+"])
print(A.result())