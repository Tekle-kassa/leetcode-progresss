/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function(points, k) {
    let s
    let obj1={}
    let arr=[]
    let res=[]
    for(let i=0;i<points.length;i++){
        s=points[i][0]**2+points[i][1]**2
        if(!obj1[s]){
            let arr2=[]
            arr2.push(points[i])
            obj1[s]=arr2
        }else{
            obj1[s].push(points[i])
        }
         arr.push(s)
    }
    arr.sort(numCompare)
    for(let i=0;i<k;i++){
        let idx=obj1[arr[i]].pop()
        res.push(idx)
    }
   
   return res
};
function numCompare(num1,num2){
    return num1-num2
}