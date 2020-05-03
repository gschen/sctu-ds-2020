class Solution:
    def twoSum(self,num:List[int],target:int) -> List[int]:
        l=[]
        for i in range(len(nums)):
            a=target-nums[i]
            if a in nums and nums.index(a)!=i:
                l.append(i)
                l.append(nums.index(a))
                break
        return l