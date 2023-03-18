/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
    nums.sort((num1,num2)=>num1-num2)
    let i=0
    let j=nums.length-1
    let counter=0
    while(i<j){
        if(nums[i]>k){
            return counter
        }
        if(nums[i]+nums[j]===k){
            counter++
            i++
            j--
        }else if(nums[i]+nums[j]>k){
            j--
        }else{
            i++
        }
    }
    return counter
};