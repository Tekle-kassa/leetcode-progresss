class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        obj=Counter(arr)
        obj=sorted(obj.values(),reverse=True)
        l,count=0,0
        while l<len(arr)/2:
            l+=obj[count]
            count+=1
        return count

            