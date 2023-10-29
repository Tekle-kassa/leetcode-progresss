class Solution {
    public void rotate(int[] nums, int k) {
        k=k%nums.length;
        reverse(nums,0,nums.length-1);
        reverse(nums,0,k-1);
        reverse(nums,k,nums.length-1);
        
    }
    public void reverse(int[]nums,int start,int end){

        for(int i=end;i>=start;i--){
            int temp = nums[start];
            nums[start] = nums[i];
            nums[i] = temp;
            start++;
        }
    }

}