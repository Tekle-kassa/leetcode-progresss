/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function(points, k) {
   points.sort((num1,num2)=>(num1[0]**2+num1[1]**2)-(num2[0]**2+num2[1]**2))
   return points.slice(0,k)
};
