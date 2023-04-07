class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        #as long as i can i will collect scores,if i cant,i want to get the maximum power so i will go to the higher tokens
        tokens.sort()
        score=0
        res=0
        i=0
        j=len(tokens)-1
        # if power<tokens[0]:
        #     return 0
        while i<=j:
            if power>=tokens[i]:
                power-=tokens[i]
                score+=1
                i+=1
            elif score>0:
                power+=tokens[j]
                score-=1
                j-=1
            else:
                return 0
            res=max(res,score)
                
        return res
                    
        
        