class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        zeros=0
        ones=0
        maxx=0
        for i in range(len(s)):
            if s[i]=='0':
                if ones!=0:
                    zeros=0
                    ones=0
                zeros+=1
            else:
                ones+=1
                if zeros!=0:
                    maxx=max(maxx,2*min(ones,zeros))
        return maxx
        