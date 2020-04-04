class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res = []
        for i in range(len(ops)):
            if ops[i] == "C":
                res.pop()
            elif ops[i] == "D":
                res.append(res[-1] * 2)
            elif ops[i] == '+':
                res.append(res[-1] + res[-2])
            else:
                res.append(int(ops[i]))
        return sum(res)
