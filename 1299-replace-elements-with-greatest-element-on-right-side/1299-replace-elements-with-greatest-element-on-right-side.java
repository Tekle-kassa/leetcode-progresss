class Solution {
    public int[] replaceElements(int[] arr) {
        int firstMax=-1;
        for(int i=arr.length-1;i>=0;i--){
            int max=Math.max(arr[i],firstMax);
            arr[i]=firstMax;
            firstMax=max;
        }
        return arr;
        
    }
    
}