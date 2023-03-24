/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let str=s.toLowerCase().replace(/[^0-9a-z]/g,'')
    let str3=''
    for(let i=str.length-1;i>=0;i--){
        str3+=str[i]
    }
    if(str3===str){
        return true
    }else return false
};