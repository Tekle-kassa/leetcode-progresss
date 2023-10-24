class Solution {
    public int[] getConcatenation(int[] nums) {
        int[]res=new int[nums.length*2];
        int i=0;
        while(i<res.length){
            if(i>=nums.length){
                res[i]=nums[i-nums.length];
            }else{
                res[i]=nums[i];
            }
            i++;
        }
        return res;
    }
}