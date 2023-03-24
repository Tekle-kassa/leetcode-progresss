class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i=len(piles)-2
        res=0
        while i>=len(piles)/3:
            res+=piles[i]
            i-=2
        return res
        