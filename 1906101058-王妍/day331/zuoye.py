class Solution(object):
    def __init__(self):
        self.stack = []
    def chengji(self,dates):
        a = list(map(str,range(100)))
        for date in dates:
            if date in a:
                self.stack.append(int(date))
            if date=='+':
                self.stack.append(sum(self.stack[-2:]))
            if date=='D':
                self.stack.append(self.stack[-1]*2)
            if date=='C':
                self.stack.pop()
    def sum_chengji(self):
        return sum(self.stack)
S=Solution()
S.chengji(["5","2","C","D","+"])
print(S.sum_chengji())
class Solution(object):
    def __init__(self):
        self.stack = []
    def chengji(self,dates):
        a = list(map(str,range(100)))
        for date in dates:
            if date in a:
                self.stack.append(int(date))
            if date=='+':
                self.stack.append(sum(self.stack[-2:]))
            if date=='D':
                self.stack.append(self.stack[-1]*2)
            if date=='C':
                self.stack.pop()
    def sum_chengji(self):
        return sum(self.stack)
S=Solution()
S.chengji(["5","2","C","D","+"])
print(S.sum_chengji())
