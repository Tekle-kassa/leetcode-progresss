class Solution {
    public int[] getConcatenation(int[] nums) {
        int[]res=new int[nums.length*2];
        int i=0;
        while(i<nums.length){
            res[i]=nums[i];
            i++;
        }
        while(i<res.length){
            res[i]=nums[i-nums.length];
            i++;
        }
        return res;
    }
}