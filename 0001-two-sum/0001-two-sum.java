class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hash = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            if (hash.containsKey(complement)) {
                return new int[]{hash.get(complement), i};
            }
            
            hash.put(nums[i], i);
        }
        
        return new int[0];
    }
}