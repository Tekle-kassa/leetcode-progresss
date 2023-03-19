class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj=defaultdict(bool)
        for k in range(len(nums)):
            if not obj[nums[k]]:
                obj[nums[k]]=[k]
            else:
                obj[nums[k]].append(k)
        nums.sort()
        store=[]
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]+nums[j]==target:
                store.append(nums[i])
                store.append(nums[j])
                break
            elif nums[i]+nums[j]<target:
                i+=1
            else:
                j-=1
        res=[]
        for k in range(2):
            res.append(obj[store[k]].pop())
        return res