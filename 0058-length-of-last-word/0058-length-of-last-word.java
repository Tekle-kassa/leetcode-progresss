class Solution {
    public int lengthOfLastWord(String s) {
        int count=0;
        int i=s.length()-1;
        
        while(i>=0) {
            if(s.charAt(i)==32){
                i--;
                continue;
            }
            
            while(i>=0){ 
                if(s.charAt(i)==32){
                    return count;
                }
                count++;
                i--;
            }
        }
        
        return count;
    }
}
