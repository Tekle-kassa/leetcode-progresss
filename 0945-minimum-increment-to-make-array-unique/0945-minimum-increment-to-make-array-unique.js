/**
 * @param {number[]} nums
 * @return {number}
 */
var minIncrementForUnique = function(nums) {
    nums.sort((a,b)=>a-b)
    let counter=0
    for(let i=0;i<nums.length;i++){
        while(nums[i]>=nums[i+1]){
            nums[i+1]+=1
            counter+=1
        }
    }
    return counter
};