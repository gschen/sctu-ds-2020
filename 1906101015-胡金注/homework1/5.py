x,y = map(int,input().split())
nums = [14,25,98,75,23,1,4,56,59]
num_x,num_y = nums[x],nums[y]
nums[y],nums[x] = num_x,num_y
print(nums)
