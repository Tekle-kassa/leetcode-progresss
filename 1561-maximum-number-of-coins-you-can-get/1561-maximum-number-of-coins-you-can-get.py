class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        freq=int(len(piles)/3)
        i=0
        j=len(piles)-1
        counter=0
        for k in range(freq):
            temp=[]
            temp.append(piles[j])
            temp.append(piles[j-1])
            temp.append(piles[i])
            counter+=temp[1]
            j-=2
            i+=1
        return counter
        