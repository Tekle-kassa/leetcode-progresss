/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    let str=s.split(' ')
    let words=new Array(str.length)
    let word,index
    for(let i=0;i<str.length;i++){
        word=str[i]
        index=word[word.length-1]
        words[index-1]=word.slice(0,-1)   
    }
    return words.join(' ')
};