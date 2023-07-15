class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        temp1=Counter(s)
        temp2=Counter(t)
        for c in temp1:
            if temp1[c]!=temp2[c]:
                return False
        return True