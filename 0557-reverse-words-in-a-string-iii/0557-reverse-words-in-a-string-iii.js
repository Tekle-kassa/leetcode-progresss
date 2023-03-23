/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    let str=''
    let l=0
    for(let i=s.length-1;i>=0;i--){
        str+=s[i]
    }
    // return str
    let words=str.split(' ')
    // console.log(words)
    let res=''
    for(let i=words.length-1;i>=0;i--){
        res+=words[i]+' '
    }
    return res.trim()
    
};