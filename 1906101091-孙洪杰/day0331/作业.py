class Solution(object):
    def calPoints(self,ops):
        sum_score=[]
        sum_score.append(int(ops[0]))
        for i in range(1,len(ops)):
            if ops[i] not in ['+','D','C']:
                sum_score.append(int(ops[i]))
            elif ops[i]=='+':
                score=sum_score[-1] + sum_score[-2]
                sum_score.append(score)
            elif ops[i]=='D':
                score=2*sum_score[-1]
                sum_score.append(score)
            else:
                sum_score.pop()
        return sum(sum_score)
s=Solution()
print(s.calPoints(['5','2','C','D','+']))  

