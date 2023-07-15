class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        temp1=defaultdict(int)
        temp2=defaultdict(int)
        for i in range(len(s)):
            if not temp1[s[i]]:
                temp1[s[i]]=1
            else:
                temp1[s[i]]+=1
            if not temp2[t[i]]:
                temp2[t[i]]=1
            else:
                temp2[t[i]]+=1
        # temp1=Counter(s)
        # temp2=Counter(t)
        for c in temp1:
            if temp1[c]!=temp2[c]:
                return False
        return True