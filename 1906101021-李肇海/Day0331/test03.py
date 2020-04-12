class Stack(object):
    def __init__(self):
        self.__list__ = []
    def push(self,date):
        self.__list__.append(date)
    def pop(self):
        return self.__list__.pop()
    def peek(self):
        return self.__init__[-1]
    def add(self):
        return sum(self.__list__)
s = Stack()
score_list = list(map(str,input().split()))
for i in score_list:
    score = 0
    if i == "+":
        score_1 = s.pop()
        score_2 = s.pop()
        score += score_1+score_2
        s.push(score_1)
        s.push(score_2)
        s.push(score)
    elif i == "D":
        score = s.peek()*2
        s.push(score)
    elif i == "C":
        s.pop()
    else:
        s.push(int(i))
print(s.add()) 

