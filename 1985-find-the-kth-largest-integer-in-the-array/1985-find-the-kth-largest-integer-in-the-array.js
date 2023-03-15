/**
 * @param {string[]} nums
 * @param {number} k
 * @return {string}
 */
var kthLargestNumber = function(nums, k) {
   
    let arr=[]
    for(let i=0;i<nums.length;i++){
        let num=BigInt(nums[i])
        if (BigInt.asIntN(Number.MAX_SAFE_INTEGER, num) !== undefined) {
            arr.push(num);
        }
    }
     arr.sort((num1, num2) => {
        if (num1 === num2) {
            return 0;
        } else if (num1 > num2) {
            return -1;
        } else {
            return 1;
        }
    }); 
    return `${arr[k-1]}`
};
