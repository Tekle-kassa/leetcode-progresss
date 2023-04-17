class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dif=len(nums)-k
        while dif<0:
            dif+=len(nums)
        temp=[]
        for i in range(dif,len(nums)):
            temp.append(nums[i])
        while dif<0:
            dif+=len(nums)
        for i in range(dif):
            temp.append(nums[i])
        i=0
        while i<len(temp):
            nums[i]=temp[i]
            i+=1