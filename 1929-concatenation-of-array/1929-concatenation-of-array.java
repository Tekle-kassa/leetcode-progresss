class Solution {
    public int[] getConcatenation(int[] nums) {
        int[]res=new int[nums.length*2];
        int i=0;
        while(i<nums.length){
            res[i]=nums[i];
            res[i+nums.length]=nums[i];
            i++;
        }
        return res;
    }
}