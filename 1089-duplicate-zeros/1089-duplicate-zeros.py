class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        nums=[]
        i=0
        j=0
        while j<len(arr) and len(nums)<=len(arr):
            if arr[i]==0:
                nums.append(0)
                if len(nums)==len(arr):
                    break
                nums.append(0)
                j+=1
            else:
                nums.append(arr[i])
            j+=1
            i+=1
        for k in range(len(nums)):
            arr[k]=nums[k]
        