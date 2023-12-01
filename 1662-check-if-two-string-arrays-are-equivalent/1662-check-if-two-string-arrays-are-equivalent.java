class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        String w1="";
        String w2="";
        int i=0;
        while(i<word1.length){
            w1+=word1[i++];
        }
        int j=0;
        while(j<word2.length){
            w2+=word2[j++];
        }
        return w1.equals(w2);
    }
}