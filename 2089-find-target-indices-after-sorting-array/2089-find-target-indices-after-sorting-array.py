class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i=0
        result=[]
        while i<len(nums) and nums[i]<=target:
            if nums[i]<target:
                i+=1
            elif nums[i]==target:
                result.append(i)
                i+=1
            else:break
        return result
            