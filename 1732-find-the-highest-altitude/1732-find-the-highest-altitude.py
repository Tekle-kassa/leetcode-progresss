class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pre=[]
        pre.append(0)
        i=0
        while i<len(gain):
            pre.append(gain[i]+pre[i])
            i+=1
        return max(pre)
        