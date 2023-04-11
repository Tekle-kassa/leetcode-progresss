class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        while i<len(haystack)-len(needle)+1:
            s=''
            for j in range(i,i+len(needle)):
                s+=haystack[j]
            if s==needle:
                return i
            i+=1
        return -1