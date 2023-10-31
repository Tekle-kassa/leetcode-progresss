class Solution {
    public void moveZeroes(int[] nums) {
        int[]temp=new int[nums.length];
        int counter=0;
        int j=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=0){
                temp[j++]=nums[i];
            }else{
                counter++;
            }
        }
        for(int i=0;i<counter;i++){
            temp[j++]=0;
        }
        for(int i=0;i<nums.length;i++){
            nums[i]=temp[i];
        }
    }
}