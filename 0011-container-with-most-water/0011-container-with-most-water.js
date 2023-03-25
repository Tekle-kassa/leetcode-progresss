/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let i=0
    let j=height.length-1
    let depth,width,area
    let maxA=0
    while(i<j){
        depth=Math.min(height[i],height[j])
        width=j-i
        area=depth*width
        maxA=Math.max(maxA,area)
        if(height[i]<height[j]){
            i++
        }else{
            j--
        }
    }
    return maxA
};