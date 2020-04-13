#给你一个 2 行 n 列的二进制数组：
#矩阵是一个二进制矩阵，这意味着矩阵中的每个元素不是 0 就是 1。
#第 0 行的元素之和为 upper。
#第 1 行的元素之和为 lower。
#第 i 列（从 0 开始编号）的元素之和为 colsum[i]，colsum 是一个长度为 n 的整数数组。
#你需要利用 upper，lower 和 colsum 来重构这个矩阵，并以二维整数数组的形式返回它。
#如果有多个不同的答案，那么任意一个都可以通过本题。
#如果不存在符合要求的答案，就请返回一个空的二维数组。
#示例 1：
# 输入：upper = 2, lower = 1, colsum = [1,1,1]
#输出：[[1,1,0],[0,0,1]]
#解释：[[1,0,1],[0,1,0]] 和 [[0,1,1],[1,0,0]] 也是正确答案。


class Solution(object):
    def __init__(self, upper, lower, colsum):
        self.upper = upper
        self.lower = lower
        self.colsum=colsum
    def reconstructMatrix(self):
        if self.upper + self.lower != sum(self.colsum):
            return []
        rows = len(self.colsum)
        ans = [[], []]
        remain_upper, remain_lower = self.upper, self.lower
        for i in range(rows):
            ans_upper = ans_lower = 0
            if self.colsum[i] == 2:
                ans_upper = ans_lower = 1
            if self.colsum[i] == 1:
                if remain_upper > remain_lower:
                    ans_upper = 1
                else:
                    ans_lower = 1

            remain_upper -= ans_upper
            remain_lower -= ans_lower
            ans[0].append(ans_upper)
            ans[1].append(ans_lower)
        return ans
m=Solution(2,2,[1,1,1])
m.reconstructMatrix()

