class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            s=''
            j=i
            while j<len(haystack) and len(s)<len(needle):
                s+=haystack[j]
                j+=1
            if s==needle:
                return i
        return -1