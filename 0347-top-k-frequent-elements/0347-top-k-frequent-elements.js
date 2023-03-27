/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let obj={}
    for(let i=0;i<nums.length;i++){
        if(!obj[[nums[i]]])obj[nums[i]]=[i]
        else obj[nums[i]].push(i)
    }
    let freq=[]
    for(let i in obj){
        freq.push([obj[i].length,parseInt(i)])
    }
    freq.sort((a,b)=>b[0]-a[0])
    let count=[]
    let j=0
    while(count.length<k){
        count.push(freq[j][1])
        j++
    }
    return count
};