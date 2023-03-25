/**
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in-place instead.
 */
var duplicateZeros = function(arr) {
    let i=0
    let k=0
    let nums=[]
    while(k<arr.length){
        if(arr[i]===0){
            nums[k]=0
            if(nums.length===arr.length){
                break
            }
            nums[k+1]=0
            k++
        }else{
            nums[k]=arr[i]
        }
        i++
        k++
    }
    for(let j=0;j<nums.length;j++){
        arr[j]=nums[j]
    }
};