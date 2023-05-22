class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp=Counter(nums)
        x=sorted(temp.items(),key=lambda item:item[1],reverse=True)
        i=0
        res=[]
        while i<k:
            res.append(x[i][0])
            i+=1
        return res
            