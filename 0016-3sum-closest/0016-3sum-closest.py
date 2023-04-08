class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        dif=inf
        ans=0
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                temp=nums[i]+nums[j]+nums[k]
                diff=abs(target-temp)
                if temp==target:
                    return temp
                elif temp>target:
                    k-=1
                else:
                    j+=1
                if diff<dif:
                    dif=diff
                    ans=temp
        return ans
                
                    
                
                
        