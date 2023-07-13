class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x
        while l<=r:
            if l*l==x:
                return l
            elif l*l<x:
                l+=1
            else:
                return l-1
        return r-1
            
        