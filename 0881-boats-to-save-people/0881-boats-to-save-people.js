/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
var numRescueBoats = function(people, limit) {
    let boats=0
    people.sort((a,b)=>a-b)
    let i=0
    let j=people.length-1
    while(i<j){
        if(people[i]+people[j]<=limit){
            boats+=1
            i++
            j--
        }else{
            boats+=1
            j--
        }
        if(i===j){
            boats+=1
        }
    }
    return boats
};