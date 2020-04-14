class Node(object):
    def __init__(self):
        self.node=[]
    def grade(self,dates):
        a=list(map(str,range(100)))
        for date in dates:
            if date in a :
                self.node.append(int(date))
            if date=='+':
                self.node.append(sum(self.node[-2:]))
            if date=='D':
                self.node.append(self.node[-1]*2)
            if date=='C':
                self.node.pop()
    def sum_grade(self):
        return sum(self.node)
a=Node()
a.grade(["5","2","C","D","+"])
print(a.sum_grade()) 