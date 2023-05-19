class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        i=1
        res=0
        while i<len(arr)-1:
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                l,r=i,i
                while l>0 and arr[l]>arr[l-1]:
                    l-=1
                while r<len(arr)-1 and arr[r]>arr[r+1]:
                    r+=1
                res=max(res,r-l+1)
                i=r
            else:
                i+=1
        return res
       
        