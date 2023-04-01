/**
 * @param {number[]} nums
 * @return {number}
 */
var minIncrementForUnique = function(nums) {
    nums.sort((a,b)=>a-b)
    let counter=0
    let i=0
    while(i<nums.length-1){
        if(nums[i]>=nums[i+1]){
            counter+=nums[i]-nums[i+1]+1
            nums[i+1]+=nums[i]-nums[i+1]+1
        }
        i++
    }
    return counter
};