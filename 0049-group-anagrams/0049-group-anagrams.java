class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        ArrayList<List<String>> res = new ArrayList<>();
        boolean[] added = new boolean[strs.length];
        for(int i=0;i<strs.length;i++){
            if (!added[i]) {
            ArrayList<String>container=new ArrayList<>();
            container.add(strs[i]);
            for(int j=i+1;j<strs.length;j++){
                if (!added[j] && isAnagram(strs[i], strs[j])) {
                    container.add(strs[j]);
                    added[j] = true;
                }
            }
            res.add(container);
            }
        }
        return res;
        
    }
        public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
        char[] sCharArray=s.toCharArray();
        char[] tCharArray=t.toCharArray();
        Arrays.sort(sCharArray);
         Arrays.sort(tCharArray);
        return Arrays.equals(sCharArray,tCharArray);
    }
}