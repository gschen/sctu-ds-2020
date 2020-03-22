#给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
#注意：答案中不可以包含重复的三元组。
#示例：
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 满足要求的三元组集合为：
# [
    #[-1, 0, 1],
  #[-1, -1, 2]
#]
nums = [-1, 0, 1, 2, -1, -4]
nums, r = sorted(nums), set()
for i in [i for i in range(len(nums)-2) if i < 1 or nums[i] > nums[i-1]]:
    d = {-nums[i]-n: j for j, n in enumerate(nums[i + 1:])}
    r.update([(nums[i], n, -nums[i]-n) for j, n in enumerate(nums[i+1:]) if n in d and d[n] > j])
    print(list(map(list, r)))
       

#给你一个正整数数组 nums，你需要从中任选一些子集，然后将子集中每一个数乘以一个 任意整数，并求出他们的和。
# 假如该和结果为 1，那么原数组就是一个「好数组」，则返回 True；否则请返回 False。
# 示例 
# 输入：nums = [12,5,7,23]
#输出：true
#解释：挑选数字 5 和 7。
# 5*3 + 7*(-2) = 1
#裴蜀定理：a,b互质的充要条件是：存在整数x,y,使ax+by=1

#法一：
nums = [12,5,7,23]      
import math
g = nums[i]
for i in nums:
    g = math.gcd(g, i)
if g==1:
  print('True')
else:
  print('False')

#reduce()函数是functools模块中的一个函数，其作用是对参数序列中元素进行累积，返回值是一个数值。
#整数的累积：列表里面整数累加
from functools import reduce
a=[1,3,5]
b=reduce(lambda x,y:x+y,a)
print('列表里面整数累加==:',b)
c=[[1,3,5],[2,4,6,8]]
d=reduce(lambda x,y:x+y,c)
print('列表里面的列表相加—:',d)
e=[("abc","123"),("def","456"),("ghi","789")]
f=reduce(lambda x,y:x+y , e )
print('列表里面的元组相加:',f)
g=['abc','def','hij']
h=reduce(lambda x,y:x+y,g)
print('列表里面字符串的累加:',h)

#法二：
import math
nums = [12,5,7,23] 
if __import__("functools").reduce(math.gcd, nums) == 1:
  print('True')
else:
  print('False')
