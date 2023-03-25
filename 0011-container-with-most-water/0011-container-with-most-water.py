class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA=0
        i=0
        j=len(height)-1
        
        while i<j:
            width=j-i
            depth=min(height[i],height[j])
            area=width*depth
            maxA=max(maxA,area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxA
        