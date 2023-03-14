/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    let i,j,count
    let res=[]
    for(i=0;i<nums.length;i++){
        count=0
        for(j=0;j<nums.length;j++){
            if(nums[i]>nums[j]){
                count+=1
            }
        }
        res.push(count)
    }
    return res
};