class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        temp=Counter(nums)
        items=temp.items()
        items=sorted(items,key=lambda x:x[1])
        # print(items)
        res=[]
        for i in range(k):
            res.append(items.pop(len(items)-1)[0])
        return res
