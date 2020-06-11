// 53. Maximum Subarray
// globalMax - initalized to -infinity
// globalMax - at every iteration, if sum >0 globalMax 
//   update globalMax

// Front - wheenver our sum is greater than 0
// Back - whenevr ou sum is less than 0

const slidingWindow = (nums)=>{
  let globalMax = Number.NEGATIVE_INFINITY; 
  let sum = 0;
  for(let front = 0; front < nums.length; front++){
    const val = nums[front]; 
    sum += val; 
    globalMax = Math.max(globalMax, sum); 
    sum = Math.max(0, sum); 
    //add value to sum.  
    //check against global max
      //if is smaller than 0, reset; 
  }
  return globalMax; 
}

const input1 = [-2,1,-3,4,-1,2,1,-5,4]
console.log(slidingWindow(input1)); 


