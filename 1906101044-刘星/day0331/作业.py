class Solution(object):
    def Points(self,ops):
        result=[]
        for i in ops:
            s=len(result)
            if i=='C':
                result.pop()
            elif i=='D':
                result.append(result[s-1]*2)
            elif i=='+':
                result.append(result[s-1]+result[s-2])
            else:
                result.append(int(i))
        return sum(result)
a=Solution()
print(a.Points(['5','2','C','D','+']))