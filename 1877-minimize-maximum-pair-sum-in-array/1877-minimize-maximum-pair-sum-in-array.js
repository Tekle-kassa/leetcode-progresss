/**
 * @param {number[]} nums
 * @return {number}
 */
var minPairSum = function(nums) {
    nums.sort((num1,num2)=>num1-num2)
    let i=0
    let j=nums.length-1
    let res=0
    while(i<j){
        if(nums[i]+nums[j]>res){
            res=nums[i]+nums[j]
        }
        i++
        j--
    }
    return res
};