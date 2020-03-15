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
       
      