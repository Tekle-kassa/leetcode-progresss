/**
 * @param {number[]} nums
 * @return {number}
 */
var minPairSum = function(nums) {
    nums.sort((num1,num2)=>num1-num2)
    let i=0
    let j=nums.length-1
    let temp=[]
    while(i<j){
        temp.push(nums[i]+nums[j])
        i++
        j--
    }
    temp.sort((num1,num2)=>num1-num2)
    return temp[temp.length-1]
};