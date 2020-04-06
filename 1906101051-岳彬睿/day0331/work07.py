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