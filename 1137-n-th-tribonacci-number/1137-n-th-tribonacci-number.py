class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        temp=[0]*(n+1)
        temp[1]=1
        temp[2]=1
        i=3
        while i<n+1:
            temp[i]=temp[i-1]+temp[i-2]+temp[i-3]
            i+=1
        return temp[n]
        
