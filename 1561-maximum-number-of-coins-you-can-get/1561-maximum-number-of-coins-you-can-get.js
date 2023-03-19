/**
 * @param {number[]} piles
 * @return {number}
 */
var maxCoins = function(piles) {
    piles.sort((num1,num2)=>num1-num2)
    let freq=piles.length/3
    let i=0
    let j=piles.length-1
    let counter=0
    console.log(piles)
    for(let k=0;k<freq;k++){
        let temp=[]
        temp.push(piles[j])
        temp.push(piles[j-1])
        temp.push(piles[i])
        console.log(temp)
        counter+=temp[1]
        j-=2
        i++
    }
    return counter
};