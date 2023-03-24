/**
 * @param {number[]} piles
 * @return {number}
 */
var maxCoins = function(piles) {
    let res=0
    piles.sort((num1,num2)=>num1-num2)
    let i=piles.length-2
    while(i>=piles.length/3){
        res+=piles[i]
        i-=2
    }
    return res
};