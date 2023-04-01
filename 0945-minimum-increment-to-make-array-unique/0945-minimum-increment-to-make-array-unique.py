class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        counter=0
        i=0
        while i<len(nums)-1:
            if nums[i]>=nums[i+1]:
                counter+=nums[i]-nums[i+1]+1
                nums[i+1]+=nums[i]-nums[i+1]+1
            i+=1
        return counter