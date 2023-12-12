class Solution {
    public int maxProduct(int[] nums) {
        int first=nums[0];
        int second=nums[1];
        if(second>first){
            int temp=first;
            first=second;
            second=temp;
        }
        int i=2;
        while(i<nums.length){
            if(nums[i]>first){
                int temp=first;
                second=first;
                first=nums[i]; 
            }else if(nums[i]>second){
                second=nums[i];
            }
            i++;
        }
        return (first-1)*(second-1);
    }
}