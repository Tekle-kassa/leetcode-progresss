/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) {
    nums.sort(numCompare)
    let i=0
    let result=[]
    while(nums[i]<=target){
        if(nums[i]<target){
            i++
        }
        else if(nums[i]===target){
            result.push(i)
            i++
        }else break
    }
    return result 
    
   
};
function numCompare(num1,num2){
    return num1-num2
}