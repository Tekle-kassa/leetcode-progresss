class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        average=-inf
        current=0
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            if i>=k-1:
                current=sum/k
                average=max(average,current)
                sum-=nums[i-(k-1)]
        return average