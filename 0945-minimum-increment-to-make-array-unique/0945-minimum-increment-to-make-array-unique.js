/**
 * @param {number[]} nums
 * @return {number}
 */
var minIncrementForUnique = function(nums) {
    nums.sort((a,b)=>a-b)
    let counter=0
    let i=0
    while(i<nums.length-1){
        if(nums[i]<nums[i+1]){
            i++
        }else{
            nums[i+1]+=1
            counter++
        }
    }
    return counter
};