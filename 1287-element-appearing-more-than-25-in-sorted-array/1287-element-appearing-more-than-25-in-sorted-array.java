class Solution {
    public int findSpecialInteger(int[] arr) {
        int len=arr.length;
        int max=len/4;
        int i=0;
        int j=i+1;
        if(arr.length==1){
            return arr[0];
        }
        while(j<arr.length){
            if(arr[j]==arr[i]){
                if(j-i+1>max){
                    return arr[j];
                }
                j++;
            }else{
                i++;
                j=i+1;
            }
        }
        return -1;
    }
}