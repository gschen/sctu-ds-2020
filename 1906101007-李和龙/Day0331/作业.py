class Stack(object):
    def __init__(self):
        self.stack = []
    def score_sum(self,Date):
        a=list(map(str,list(range(101))))
        for date in Date:
            if date in a:
                self.stack.append(int(date))
            if date=='+':
                self.stack.append(sum(self.stack[-2:]))
            if date=='D':
                self.stack.append((self.stack[-1])*2)
            if date=='C':
                self.stack=self.stack[:-1]
    def result(self):
        return sum(self.stack)
A=Stack()
A.score_sum(["5","2","C","D","+"])
print(A.result())