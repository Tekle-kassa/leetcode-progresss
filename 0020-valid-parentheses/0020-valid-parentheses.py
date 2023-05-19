class Solution:
    def isValid(self, s: str) -> bool:
        res=[]
        obj={')':'(',']':'[','}':'{'}
        for p in s:
            if p in obj: 
                if res and res[len(res)-1]==obj[p]:
                    res.pop()
                else:return False
            else:
                res.append(p)
        if not res:
            return True
        return False
            
                
        