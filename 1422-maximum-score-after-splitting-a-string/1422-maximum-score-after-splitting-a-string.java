class Solution {
    public int maxScore(String s) {
        int result=0;
        for(int i=0;i<s.length()-1;i++){
            int temp=0;
            for(int j=0;j<=i;j++){
                if(s.charAt(j)=='0'){
                    temp++;
                }
                
            }
            for(int j=i+1;j<s.length();j++){
                if(s.charAt(j)=='1'){
                    temp++;
                }
            }
            result=Math.max(result,temp);
        }
        return result;
    }
}