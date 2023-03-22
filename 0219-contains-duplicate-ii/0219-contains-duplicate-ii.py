class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        obj=defaultdict(bool)
        for i in range(len(nums)):
            if not obj[nums[i]]:
                obj[nums[i]]=[i]
            else:
                obj[nums[i]].append(i)
        nums.sort()
        
        for i in range(len(nums)):
            if i+1<len(nums):
                if nums[i]==nums[i+1]:
                    for j in range(len(obj[nums[i]])):
                        if j+1<len(obj[nums[i]]):
                            if abs(obj[nums[i]][j+1]-obj[nums[i]][j])<=k:
                                return True
        return False
        