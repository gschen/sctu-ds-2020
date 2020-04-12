# 你现在是网球比赛记录员。
# 给定一个字符串列表，每个字符串可以是以下四种类型之一：
# 1.整数：您在本轮中获得的积分数。
# 2. "+"：表示本轮获得的得分是前两轮有效 回合得分的总和。
# 3. "D"：表示本轮获得的得分是前一轮有效 回合得分的两倍。
# 4. "C"：表示您获得的最后一个有效 回合的分数是无效的，应该被移除。

# 每一轮的操作都是永久性的，可能会对前一轮和后一轮产生影响。
# 你需要返回你在所有回合中得分的总和。
class Solution(object):
    def score(self,range):
        stack = []
        for i in range:
            if i == 'C':
                stack.pop()
            elif i == 'D':
                stack.append(stack[-1]*2)
            elif i == '+':
                stack.append(stack[-1] + stack[-2])
            else:
               stack.append(int(i))
        return sum(stack)
s = Solution()
sum = s.score(['5','2','C','D','+'])
print(sum)