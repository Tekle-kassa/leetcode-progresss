# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        min_=1
        max_=n
        mid=(min_+max_)//2
        res=guess(mid)
        while res!=0:
            if res==1:
                min_=mid
                mid=(min_+max_+1)//2
                res=guess(mid)
            elif res==-1:
                max_=mid
                mid=(min_+max_)//2
                res=guess(mid)
        return mid
        
            
            
         
         
        