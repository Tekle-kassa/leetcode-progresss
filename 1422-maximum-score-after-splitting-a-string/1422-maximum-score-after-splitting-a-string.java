class Solution {
    public int maxScore(String s) {
        int ones=0;
        int ans=0;
        int zeros=0;
        int i=0;
        while(i<s.length()){
            if(s.charAt(i)=='1'){
                ones++;
            }
            i++;
        }   
        for(int j=0;j<s.length()-1;j++){
            if(s.charAt(j)=='0'){
                zeros++;
            }else{
                ones--;
            }
            ans=Math.max(ans,zeros+ones);
        }
        return ans;
    }
}