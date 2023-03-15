class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr=[]
        for i in range(len(nums)):
            arr.append(int(nums[i]))
        arr.sort()
        arr.reverse()
        return f'{arr[k-1]}'