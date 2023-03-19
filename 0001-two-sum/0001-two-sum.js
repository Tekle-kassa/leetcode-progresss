/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let i=0
    let j=nums.length-1
    let obj1={}
    let ans=[]
    for(let k=0;k<nums.length;k++){
        if(!obj1[nums[k]]){
            let arr2=[]
            arr2.push(k)
            obj1[nums[k]]=arr2    
        }else{
            obj1[nums[k]].push(k)
        }
    }
    nums.sort(numCompare)
    let store=[]
    while(i<j){
        if(nums[i]+nums[j]===target){
            store.push(nums[i])
            store.push(nums[j])
            break
        }else if(nums[i]+nums[j]<target){
            i++
        }else j --
    }
    for(let k=0;k<2;k++){
        let idx=obj1[store[k]].pop()
        ans.push(idx)
    }
    return ans
};
function numCompare(num1,num2){
       return num1-num2
}