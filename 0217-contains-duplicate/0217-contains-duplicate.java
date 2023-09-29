class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        int i=0;
        while(i+1<nums.length){
            if(nums[i]==nums[i+1]){
                return true;
            }
            i+=1;
        }
        return false;
    }
}