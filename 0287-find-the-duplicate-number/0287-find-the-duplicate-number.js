/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    nums.sort((num1,num2)=>num1-num2)
    for(let i=0;i<nums.length;i++){
        if(nums[i]===nums[i+1]){
            return nums[i]
        }
    }
};