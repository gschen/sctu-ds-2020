#sys的看内存占用情况函数
import sys
print(sys.getsizeof('python'))

#给你一个 2 行 n 列的二进制数组：
#矩阵是一个二进制矩阵，这意味着矩阵中的每个元素不是 0 就是 1。
#第 0 行的元素之和为 upper。
#第 1 行的元素之和为 lower。
#第 i 列（从 0 开始编号）的元素之和为 colsum[i]，colsum 是一个长度为 n 的整数数组。
#你需要利用 upper，lower 和 colsum 来重构这个矩阵，并以二维整数数组的形式返回它。
#如果有多个不同的答案，那么任意一个都可以通过本题。
#如果不存在符合要求的答案，就请返回一个空的二维数组。

upper = 2
lower = 1
colsum = [1,1,1]
rows=[1]*upper+[0]*(len(colsum)-upper)
cols=[m-n for n,m in zip(rows,colsum)]
print([rows,cols] if sum(cols)==lower else [])

