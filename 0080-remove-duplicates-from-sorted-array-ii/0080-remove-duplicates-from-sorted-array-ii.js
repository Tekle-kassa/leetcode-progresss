/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
  let curr = 2;
    
    for (let i = 2; i < nums.length; i++) {
        if (nums[i] !== nums[curr - 2]) {
            nums[curr] = nums[i];
            curr++;
        }
    }
    
    return curr;
};