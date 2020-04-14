class Solution(object):
    def game(self,sor):
        result=[]
        for i in sor:
            a=len(result)
            if i=="+":
                result.append(result[a-1]+result[a-2])
            elif i=="C":
                result.pop()
            elif i=="D":
                result.append(result[a-1]*2)
            else:
                result.append(int(i))
        return sum(result)
s=Solution()
print(s.game(["5","2","C","D","+"]))