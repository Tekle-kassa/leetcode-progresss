/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    let obj={}
  for(let i=0;i<nums.length;i++){
      if(!obj[nums[i]]){
          obj[nums[i]]=[i]
      }else{
          obj[nums[i]].push(i)
      }
  }
    // console.log(obj)
    nums.sort((num1,num2)=>num1-num2)
    // console.log(nums)
    for(let i=0;i<nums.length;i++){
        if(nums[i]===nums[i+1]){
            for(let j=0;j<obj[nums[i]].length;j++){
                if(Math.abs(obj[nums[i]][j+1]-obj[nums[i]][j])<=k){
                    return true
                }
            }
        }        
    }
    return false
};