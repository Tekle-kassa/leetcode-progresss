class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq=[]
        obj=Counter(arr)
        s_obj=sorted(obj.items(),reverse=True,key=lambda x:x[1])
        l=0
        j=0
        count=0
        while l<len(arr)/2:
            l+=s_obj[j][1]
            count+=1
            j+=1
        return count