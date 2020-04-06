class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res=[]
        sum=0 
        res.append(ops[0])
        sum=sum+int(res[-1])
        for i in range(1,len(ops)):
            if ops[i]=='+':
                res.append(int(res[-1])+int(res[-2]))
                sum=sum+int(res[-1])
            elif ops[i]=='D':
                res.append(int(res[-1])*2)
                sum=sum+int(res[-1])
            elif ops[i]=='C':
                sum=sum-int(res[-1])
                res.pop()
            else :
                res.append(ops[i])
                sum=sum+int(res[-1])
        return sum
