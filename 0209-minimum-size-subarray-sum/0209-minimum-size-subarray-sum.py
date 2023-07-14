class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=0
        current=0
        minSize=float('inf')
        for i in range(len(nums)):
            current+=nums[i]
            while current>=target:
                minSize=min(minSize,i-start+1)
                current-=nums[start]
                start+=1
        if minSize==float('inf'):return 0
        return minSize
        