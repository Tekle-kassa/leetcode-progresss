class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[j]+nums[k]+nums[i]==0:
                    res.add((nums[j],nums[i],nums[k]))
                    j+=1
                    k-=1
                elif nums[j]+nums[k]+nums[i]<0:
                    j+=1
                else:
                    k-=1
        # ans=[list(i) for i in res]
        ans=[]
        for i in res:
            ans.append(list(i))
        return ans
                