class Solution {
    public int lengthOfLastWord(String s) {
        char space=' ';
        int count=0;
        int i=s.length()-1;
        
        while(i>=0) {
            if(s.charAt(i)==space) {
                i--;
                continue;
            }
            
            while(i>=0){ 
                if(s.charAt(i)==space){
                    return count;
                }
                count++;
                i--;
            }
        }
        
        return count;
    }
}
