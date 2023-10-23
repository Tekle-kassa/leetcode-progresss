class Solution {
    public int maxArea(int[] height) {
        int i=0;
        int j=height.length-1;
        int maxA=0;
        while(i<j){
            int dif=j-i;
            int depth=Math.min(height[i],height[j]);
            maxA=Math.max(maxA,depth*dif);
            if(height[j]>height[i]){
                i++;
            }else{
                j--;
            }
        }
        return maxA;
    }
}