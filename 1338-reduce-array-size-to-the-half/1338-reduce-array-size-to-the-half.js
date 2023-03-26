/**
 * @param {number[]} arr
 * @return {number}
 */
var minSetSize = function(arr) {
    let freq=[]
    let mySet=new Set()
    let obj={}
    for(let i=0;i<arr.length;i++){
        if(!obj[arr[i]]){
            obj[arr[i]]=[i]
        }else{
            obj[arr[i]].push(i)
        }
    }
    // console.log(obj)
    for(let i in obj){
        freq.push([obj[i].length,parseInt(i)])
    }
     freq.sort((num1,num2)=>num2[0]-num1[0])
    // console.log(freq)
    let j=0
    let len=0
    let count=0
    while(len<arr.length/2){
        // console.log(freq[j][0])
       len+=freq[j][0]
        count++
        j++
    }
    return count

    
};