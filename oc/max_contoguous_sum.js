// Max contiguous sum - must use at least one element 
//Given an array of integers (positive and negative) 
//return the largest continguous sum
//Make biggest conintus window sum
/*

if a window's sum drops below zero, start over

want to check against global max each step

[1,2,3,4] => 10

[1,2,-5, 3,4] => 7
 1 3 -2, 0+3, 
 
 [1,2,5,3,4] => 15
 
 globalMax = -2
 currentSum = 0
 [  -2  , -8,   -10] -> 
     -2    -8   -10

*/
// Number.NEGATIVE_INFINITY
const findLargestSum = (inputs)=>{
  let globalMax = Number.NEGATIVE_INFINITY;
  let currentSum = 0;
  
  for(let i = 0;  i < inputs.length; i++){
    const val = inputs[i]; 
    currentSum += val;
    
    globalMax = Math.max(currentSum, globalMax); 
    currentSum = Math.max(currentSum, 0); 
  }
  return globalMax;
}

console.log(findLargestSum([1,2,3,4]))
console.log(findLargestSum([1,2,-5,3,4]))
console.log(findLargestSum([-2,-8,-10]))