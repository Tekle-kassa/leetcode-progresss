class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums1)):
            j=0
            while nums1[i]!=nums2[j]:
                j+=1
            k=j+1
            if k==len(nums2):
                res.append(-1)
            while k<len(nums2):
                if nums2[k]>nums2[j]:
                    res.append(nums2[k])
                    break
                else:
                    if k+1==len(nums2):
                        res.append(-1)
                k+=1
        return res
                    
        