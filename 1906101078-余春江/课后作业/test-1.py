#求给定数的阶乘，要求：所求阶乘的数不可以是这几个数：[1，10,20,30,40,50].
n = int(input())
nums = [1,10,20,30,40,50]
def jiecheng(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * jiecheng(n-1)
if n in nums:
    print(False)
else:
    print(jiecheng(n))
