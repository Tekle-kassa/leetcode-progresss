/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    for(let i=0;i<nums.length;i++){
        let j=i+1
        while(nums[i]===nums[j]){
            j++
        }
        nums.splice(i+1,j-i-1)
        
    }
    return nums.length
    
};
