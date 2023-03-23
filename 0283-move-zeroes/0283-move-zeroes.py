class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        counter=0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i]=nums[j]
                i+=1
            else:
                counter+=1
            # print(nums)
        
        for j in range(counter):
            nums[len(nums)-1-j]=0
        # print(nums)
       