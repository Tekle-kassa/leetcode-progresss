class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr=[]
        arr.append(nums[0])
        # for i in range(1,len(nums)):
        #     arr.append(nums[len(nums)-i])
        #     arr.append(nums[i])
        i=1
        while len(arr)<len(nums):
            arr.append(nums[len(nums)-i])
            if len(arr)==len(nums):
                break
            arr.append(nums[i])
            i+=1
            
        return arr