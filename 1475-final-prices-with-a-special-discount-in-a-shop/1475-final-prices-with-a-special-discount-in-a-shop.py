class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res=[]
        for i in range(len(prices)):
            j=i+1
            while j<len(prices) and prices[j]>prices[i]:
                j+=1
            if j==len(prices):
                res.append(prices[i])
            else:
                res.append(prices[i]-prices[j])
        return res