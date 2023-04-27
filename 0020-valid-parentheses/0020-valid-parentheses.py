class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        if s[0]!='[' and s[0]!='{' and s[0]!='(':
            return False
        res=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                res.append(s[i])
            elif s[i]==')':
                if len(res)>0 and res[len(res)-1]=='(':
                    res.pop()
                else:
                    return False
            elif s[i]==']':
                if len(res)>0 and res[len(res)-1]=='[':
                    res.pop()
                else:
                    return False
            elif s[i]=='}':
                if len(res)>0 and res[len(res)-1]=='{':
                    res.pop()
                else:
                    return False
        if len(res)==0:
            return True
        return False
                
            