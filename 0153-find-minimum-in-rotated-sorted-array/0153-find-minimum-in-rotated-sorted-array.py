class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        res=nums[0]
        if len(nums)==1 or nums[0]<nums[len(nums)-1]:
            return nums[0]
        while l<=r:
            if nums[l]<nums[r]:
                res=min(res,nums[l])
                break
            mid=(l+r)//2
            res=min(res,nums[mid])
            if nums[mid]>=nums[l]:
                l=mid+1
            else:
                r=mid-1
        return res