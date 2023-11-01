class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int r=nums1.length-1;
        int i=m-1;
        int j=n-1;
        while(i>=0 && j>=0){
            if(nums1[i]<nums2[j]){
                nums1[r]=nums2[j];
                j--;
            }else{
                nums1[r]=nums1[i];
                i--;
            }
            r--;
        }
        while(j>=0){
            nums1[r--]=nums2[j--];
        }
    }
}