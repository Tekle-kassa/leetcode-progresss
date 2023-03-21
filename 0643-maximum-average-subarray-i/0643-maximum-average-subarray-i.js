/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let average=-Number.MAX_VALUE
    let current=0
    let sum=0
    for(let i=0;i<nums.length;i++){
        sum+=nums[i]
        if(i>=k-1){
            current=sum/k
            average=Math.max(average,current)
            sum-=nums[i-(k-1)]
        }
    }
    return average
};