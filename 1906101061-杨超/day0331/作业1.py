'''你现在是网球比赛记录员。
给定一个字符串列表，每个字符串可以是以下四种类型之一：
1.整数：您在本轮中获得的积分数。
2. "+"：表示本轮获得的得分是前两轮有效 回合得分的总和。
3. "D"：表示本轮获得的得分是前一轮有效 回合得分的两倍。
4. "C"：表示您获得的最后一个有效 回合的分数是无效的，应该被移除。

每一轮的操作都是永久性的，可能会对前一轮和后一轮产生影响。
你需要返回你在所有回合中得分的总和。

示例 1:

输入: ["5","2","C","D","+"]
输出: 30
解释: 
第1轮：你可以得到5分。目前总分是：5。
第2轮：你可以得到2分。目前总分是：7。
第3轮：第2轮的数据无效。目前总分是：5。
第4轮：你可以得到10分（第2轮的数据已被删除）。总数是：15。
第5轮：你可以得到5 + 10 = 15分。总数是：30。'''
class Solution(object):
    def calPoints(self,ops):

        result=[]
        for i in ops:
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
print(a.calPoints(["5","2","C","D","+"]))