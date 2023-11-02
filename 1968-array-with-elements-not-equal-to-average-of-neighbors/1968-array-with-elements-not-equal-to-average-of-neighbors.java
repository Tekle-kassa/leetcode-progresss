
public class Solution {
    public int[] rearrangeArray(int[] nums) {
        Arrays.sort(nums);
        List<Integer> temp = new ArrayList<>();
        temp.add(nums[0]);
        int i = 1;
        while (temp.size() < nums.length) {
            temp.add(nums[nums.length - i]);
            
            if (temp.size() == nums.length) {
                break;
            }
            
            temp.add(nums[i]);
            i++;
        }
        
        int[] result = new int[temp.size()];
        for (int j = 0; j < temp.size(); j++) {
            result[j] = temp.get(j);
        }
        
        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {5, 4, 3, 2, 1};
        int[] rearranged = solution.rearrangeArray(nums);
        System.out.println(Arrays.toString(rearranged));
    }
}
