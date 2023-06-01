class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(l,r):
            if l<r:
                s[l],s[r]=s[r],s[l]
                return rev(l+1,r-1)
        rev(0,len(s)-1)