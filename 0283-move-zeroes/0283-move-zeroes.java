class Solution {
    public void moveZeroes(int[] nums) {
        int l=0;
        int counter=0;
        for(int r=0;r<nums.length;r++){
            if(nums[r]!=0){
                nums[l]=nums[r];
                l++;
            }
            else{
                counter++;
            }
        }
        for(int i=0;i<counter;i++){
            nums[nums.length-1-i]=0;
        }
    }
}