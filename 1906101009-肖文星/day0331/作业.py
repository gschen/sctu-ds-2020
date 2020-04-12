class Solution():
    def calPoints(self, yy):
        """
        :type yy: List[str]
        :rtype: int
        """
        res = []
        for i in range(len(yy)):
            if yy[i] == "C":
                res.pop()
            elif yy[i] == "D":
                res.append(res[-1] * 2)
            elif yy[i] == '+':
                res.append(res[-1] + res[-2])
            else:
                res.append(int(yy[i]))
        return sum(res)
a=Solution()
print(a.calPoints(['2','2','5']))
