/**
 * @param {number[]} nums
 * @param {number[]} l
 * @param {number[]} r
 * @return {boolean[]}
 */
var checkArithmeticSubarrays = function(nums, l, r) {
    let temp=[]
    let res=[]
    
    for(let i=0;i<l.length;i++){
        let j=0,k=1
        temp=nums.slice(l[i],r[i]+1)
        temp.sort((num1,num2)=>num1-num2)
        console.log(temp)
        if(temp.length===2){
            res.push(true)
            continue
        }
        while(k+1<temp.length){
            if(temp[k]-temp[j]===temp[k+1]-temp[k]){
                j++
                k++
                if(k+1===temp.length){
                    res.push(true)
                    // j=0
                    // k=1
                }
                
            }else{
                res.push(false)
                // j=0
                // k=1
                break
            }    
        }
        
        
    }
    return res
};