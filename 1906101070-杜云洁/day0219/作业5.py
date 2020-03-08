#交换列表中的任意两个元素：[14,25,98,75,23,1,4,56,59](要求，被置换的两个位置需要input输入)
import random
nums=[14,25,98,75,23,1,4,56,59]
a=int(input())
b=int(input())
nums[a],nums[b]=nums[b],nums[a]
print(nums)


