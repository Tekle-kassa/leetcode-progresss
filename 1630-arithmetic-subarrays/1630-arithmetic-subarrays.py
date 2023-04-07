class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]
        i=0
        j=0
        while i in range(len(l)):
            temp=[]
            for j in range(l[i],r[i]+1):
                temp.append(nums[j])
            temp.sort()
            k=1
            if len(temp)==2:
                ans.append(True)
            while k+1<len(temp):
                if temp[k]-temp[k-1]==temp[k+1]-temp[k]:
                    k+=1
                    if k+1==len(temp):
                        ans.append(True)
                else:
                    ans.append(False)
                    break
            i+=1
        return ans
                

        
        