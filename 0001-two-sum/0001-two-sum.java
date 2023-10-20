class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, List<Integer>> obj = new HashMap<>();

        for (int k = 0; k < nums.length; k++) {
            if (!obj.containsKey(nums[k])) {
                obj.put(nums[k], new ArrayList<>());
            }
            obj.get(nums[k]).add(k);
        }

        Arrays.sort(nums);

        List<Integer> store = new ArrayList<>();
        int i = 0;
        int j = nums.length - 1;

        while (i < j) {
            if (nums[i] + nums[j] == target) {
                store.add(nums[i]);
                store.add(nums[j]);
                break;
            } else if (nums[i] + nums[j] < target) {
                i++;
            } else {
                j--;
            }
        }

        int[] res = new int[2];
        for (int k = 0; k < 2; k++) {
            res[k] = obj.get(store.get(k)).remove(obj.get(store.get(k)).size() - 1);
        }

        return res;
    }
}

