class Solution {
    public boolean isPathCrossing(String path) {
        int x=0;
        int y=0;
        Set<String> temp=new HashSet<>();
        temp.add(x+","+y);
        for(int i=0;i<path.length();i++){
            if(path.charAt(i)=='N'){
                y++;
            }else if(path.charAt(i)=='S'){
                y--;
            }
            else if(path.charAt(i)=='E'){
                x++;
            }
            else if(path.charAt(i)=='W'){
                x--;
            }
            if(temp.contains(x+","+y)){
                return true;
            }else{
                temp.add(x+","+y);
            }
        }
        return false;
    }
}