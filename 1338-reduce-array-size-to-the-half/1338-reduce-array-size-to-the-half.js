/**
 * @param {number[]} arr
 * @return {number}
 */
var minSetSize = function(arr) {
    let freq=[]
    let obj={}
    for(let i=0;i<arr.length;i++){
        if(!obj[arr[i]]){
            obj[arr[i]]=[i]
        }else{
            obj[arr[i]].push(i)
        }
    }
    for(let i in obj){
        freq.push([obj[i].length,parseInt(i)])
    }
    
    freq.sort((num1,num2)=>num2[0]-num1[0])
    let len=0
    let count=0
    while(len<arr.length/2){
       len+=freq[count][0]
        count++
    }
    return count

    
};