class Solution {
    public int[] replaceElements(int[] arr) {
        int[]out=new int[arr.length];
        int max=0;
        for(int i=0;i<arr.length-1;i++){
            max=arr[i+1];
            for(int j=i+1;j<arr.length;j++){
                if(arr[j]>max){
                    max=arr[j];
                }
            }
            out[i]=max;
        }
        out[out.length-1]=-1;
        return out;
    }
    
}