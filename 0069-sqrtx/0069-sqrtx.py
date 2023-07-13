class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x // 2
        if x==1:
            return 1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
        return r
        