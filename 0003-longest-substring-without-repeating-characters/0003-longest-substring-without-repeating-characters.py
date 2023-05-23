class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r=1
        temp=''
        if len(s)>=1:
            temp+=s[0]
            count=1
            while r<len(s):
                # print(temp)
                
                if s[r] in temp:
                    i=0
                    while s[r]!=temp[i]:
                        i+=1
                    temp=temp[i+1:]
                    # print(temp)
                    temp+=s[r]
                else:
                    temp+=s[r]
                    # print(temp)
                r+=1
                count=max(count,len(temp))
            return count
        return 0
                