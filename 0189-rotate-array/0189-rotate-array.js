/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    let res=[]
    let n=nums.length-k
    
    while(n<0){
        n+=nums.length
    }
    for(let i=n;i<nums.length;i++){
        res.push(nums[i])
    }
    // console.log(res)
    let diff=nums.length-k
    while(diff<0){
        diff+=nums.length
    }
    for(let j=0;j<diff;j++){
        res.push(nums[j])
    }
    for(let i=0;i<res.length;i++){
        nums[i]=res[i]
    }
};