class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n=len(arr)
        i=1
        ans=0
        while i<=n-2:
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                j=i
                # count=1
                while j>0 and arr[j]>arr[j-1]:
                    j-=1
                    # count+=1
                while i<n-1 and arr[i]>arr[i+1]:
                    i+=1
                    # count+=1
                ans=max(ans,i-j+1)
            else:
                i+=1
        return ans