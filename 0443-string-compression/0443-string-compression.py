class Solution:
    def compress(self, chars: List[str]) -> int:
        s=''
        j=0
        while j<len(chars):
            i=j+1
            count=1
            while i<len(chars) and chars[j]==chars[i]:
                count+=1
                i+=1
            if count>1:
                s+=chars[j]
                s+=str(count)
            else:
                s+=chars[j]
            j=i
        for i in range(len(s)):
            chars[i]=s[i]
        return len(s)   
                
            
            
        