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
    for(let i in obj){
        // console.log(obj[i])
        if(obj[i].length>1){
            for(let j=0;j<obj[i].length;j++){
                if(obj[i][j+1]-obj[i][j]<=k){
                    return true
                }
            }
        } 
    }
    return false
   
};