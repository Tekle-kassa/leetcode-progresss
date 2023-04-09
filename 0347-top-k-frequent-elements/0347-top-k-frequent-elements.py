class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        temp=Counter(nums)
        freq=temp.most_common()
        res=[]
        i=0
        while i<k:
            res.append(freq[i][0])
            i+=1
        return res
