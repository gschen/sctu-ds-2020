class Sit():
    def __init__(self,score = []):
        self.score = score
         self.num = []
class Solution():
    def travel(self):
        for s in self.score:
            if s == '+':
                self.num.append(self.num[-1]+self.num[-2])
            elif s == 'D':
                self.num.append(self.num[-1]*2)
            elif s == 'C':
                self.num.pop()
            else:
                self.num.append(int(s))

    return sum(num)

sl = Sit(['2','2','5'])
sa = Solution()
print(sa.travel())

            




