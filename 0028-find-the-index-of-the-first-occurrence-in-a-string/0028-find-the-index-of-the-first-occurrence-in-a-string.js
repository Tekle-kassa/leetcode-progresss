/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    for(let i=0;i<haystack.length;i++){
        let s=''
        let j=i
        // for(let j=i;s.length>=needle.length;j++){
        //     s+=haystack[j]
        // }
        while(s.length<needle.length){
            s+=haystack[j]
            j++
        }
        if(s===needle){
            return i
        }
    }
    return -1
        
}