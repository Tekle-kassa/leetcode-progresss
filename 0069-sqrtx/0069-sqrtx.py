class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=1,x//2
        if x==1:return 1
        while l<=r:
            mid=(l+r)//2
            if mid**2<x:
                l=mid+1
            elif mid**2>x:
                r=mid-1
            else:
                return mid
        return r
        