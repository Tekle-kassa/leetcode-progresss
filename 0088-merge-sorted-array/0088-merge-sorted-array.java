class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i=0;
        int j=0;
        int[]temp=new int[nums1.length];
        int count=0;
        while(j<n && i<m){
            if(nums1[i]<nums2[j]){
                temp[count]=nums1[i++];
            }
            else{
                temp[count]=nums2[j];
                j++;
            }
            count++;
        }
        if(i<m){
            while(count<temp.length){
                temp[count++]=nums1[i++];
            }
        }else if(j<n){
            while(count<temp.length){
                temp[count++]=nums2[j++];
            }
        }
        for(int k=0;k<temp.length;k++){
            nums1[k]=temp[k];
        }
    }
}