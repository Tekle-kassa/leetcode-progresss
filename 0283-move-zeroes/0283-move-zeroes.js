/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let j=0
    let counter=0
    for(let i=0;i<nums.length;i++){
        if(nums[i]!==0){
            nums[j]=nums[i]
            j++
        }else{
            counter++
        }
    }
    for(let i=0;i<counter;i++){
        nums[nums.length-1-i]=0
    }
};