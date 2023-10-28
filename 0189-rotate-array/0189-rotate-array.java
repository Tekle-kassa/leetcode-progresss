class Solution {
    public void rotate(int[] nums, int k) {
        int[]res=new int[nums.length];
        int count=0;
        int st=nums.length-k;
        while(st<0){
            st+=nums.length;
        }
        for(int i=st;i<nums.length;i++){
            res[count++]=nums[i];
        }
        for(int i=0;i<st;i++){
            res[count++]=nums[i];
        }
        for(int i=0;i<nums.length;i++){
            nums[i]=res[i];
        }
    }

}