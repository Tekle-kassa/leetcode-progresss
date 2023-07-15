class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        temp1=Counter(s)
        temp2=Counter(t)
        return temp1==temp2