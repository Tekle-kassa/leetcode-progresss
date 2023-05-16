class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dif=k%len(nums)
        temp1=nums[:len(nums)-dif]
        temp2=nums[len(nums)-dif:]
        for i in range(len(temp2)):
            nums[i]=temp2[i]
        for i in range(len(temp1)):
            nums[i+dif]=temp1[i]