/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  let obj={}
  for(let i=0;i<nums.length;i++){
      let temp=[]
      if(!obj[nums[i]]){
          temp.push(i)
          obj[nums[i]]=temp
      }else{
          obj[nums[i]].push(i)
      }
  }
    let j=0
    let k=nums.length-1
    nums.sort((num1,num2)=>num1-num2)
    let store=[]
    while(j<k){
        if(nums[j]+nums[k]===target){
            store.push(nums[j])
            store.push(nums[k])
            break
        }else if(nums[j]+nums[k]<target) j++
        else k--
    }
    let res=[]
    for(let i=0;i<2;i++){
        let idx=obj[store[i]].pop()
        res.push(idx)
    }
    return res
};
