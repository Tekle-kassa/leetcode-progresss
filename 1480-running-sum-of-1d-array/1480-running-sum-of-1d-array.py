class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre=[]
        pre.append(nums[0])
        i=1
        while len(pre)<len(nums):
            pre.append(pre[i-1]+nums[i])
            i+=1
        return pre