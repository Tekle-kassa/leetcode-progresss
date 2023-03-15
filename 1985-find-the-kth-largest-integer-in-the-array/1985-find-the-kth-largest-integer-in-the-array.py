class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr=[]
        str=''
        for i in range(len(nums)):
            arr.append(int(nums[i]))
        arr.sort()
        arr.reverse()
        str+=f'{arr[k-1]}'
        return str