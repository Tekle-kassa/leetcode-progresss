class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        max_=0
        while l<r:
            length=r-l
            h=min(height[l],height[r])
            max_=max(max_,length*h)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return max_