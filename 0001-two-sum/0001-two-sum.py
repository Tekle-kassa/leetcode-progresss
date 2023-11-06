class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pMap={}
        for i in range(len(nums)):
            v=nums[i]
            dif=target-v
            if dif in pMap:
                return [pMap[dif],i]
            pMap[v]=i
            