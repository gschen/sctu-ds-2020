class Solution:
    def calPoints(self, ops):
        last = []
        for i in ops:
            if i is "C":
                last.pop()
            elif i is "D":
                last.append(last[-1] * 2)
            elif i is "+":
                last.append(last[-1] + last[-2])
            else:
                last.append(int(i))
        return sum(last)

#