/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    let str=s.split(' ')
    let result=new Array(str.length)
    let words=new Array(str.length)
    for(let i=0;i<str.length;i++){
        let word=str[i]
        let index=word[word.length-1]
        words[index-1]=word
        let ind=words[index-1]
        result[index-1]=(ind.slice(0,-1))    
    }
    return result.join(' ')
};