class Solution {
    public int minimumDifference(int[] nums, int k) {
        Arrays.sort(nums);
        int dif=Integer.MAX_VALUE;
        int l=0;
        int r=k-1;
        while(r<nums.length){
            dif=Math.min(dif,nums[r]-nums[l]);
            l++;
            r++;
        }
        return dif;
    }
}