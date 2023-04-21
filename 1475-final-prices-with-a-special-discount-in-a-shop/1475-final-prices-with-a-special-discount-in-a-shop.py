class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        stack = []
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                res[stack.pop()] -= prices[i]
            res.append(prices[i])
            stack.append(i)
        return res