class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        obj=defaultdict(bool)
        for i in range(len(nums)):
            if not obj[nums[i]]:
                obj[nums[i]]=[i]
            else:
                obj[nums[i]].append(i)
        freq=[]
        for i in obj:
            freq.append([len(obj[i]),int(i)])
        freq.sort(reverse=True)
        j=0
        res=[]
        while len(res)<k:
            res.append(freq[j][1])
            j+=1
        return res