
class Solution(object):
    def Cal(self,sor):
        result=[]
        for i in sor:
            s=len(result)
            if i=="+":
                result.append(result[s-1]+result[s-2])
            elif i=="C":
                result.pop()
            elif i=="D":
                result.append(result[s-1]*2)
            else:
                result.append(int(i))
        return sum(result)
a=Solution()
print(a.Cal(["5","2","C","D","+"]))
1