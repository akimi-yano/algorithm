// Equal sum partition 
// input array postive ints [] ->  true 
// Return true if we can break it up into 2 parts of equal sum

// [10,| 5, 3,2]  - 20 true
// [10, 7, 3, 2]  - 22 false

// target number == total sum / 2
  //if the largest number > target, we can't solve
  //if the target is odd then we can return false
  
  //base cases,
    // current sum > target -- stop
    // current sum == target -- success!
    // ran out of elements
    
    /*
                  0,0 -  8
                /       \  
       0-1       0          1 
             / \         /  \
       1-1    0   2       1     3
       2-3
       3-5
       4-4
       
    
    */
    
const example1 = [3,2,1,5,4,1]//true -> [5,3] [4,1,1,2]
const example2 = [1,2,3,5,4]//false 
const example3 = [] //? -> [] [] 

const equalSizePartition = (inputArr)=>{
  let max = 0; 
  let sum = 0; 
  for(let i = 0; i < inputArr.length; i++){
    max = Math.max(inputArr[i], max);
    sum += inputArr[i]; 
  }
  let target = sum / 2; 
  if(sum % 2 == 1)
    return false; 
  if(max > target)
    return false; 
  const cache = {}; 
  const traverse = (index, total)=>{
    if(total == target)
      return true; 
    if(index >= inputArr.length || total > target)
      return false; 
    const key = `${index}-${total}`
    if(cache[key])
      return cache[key]
    //traverse and increase total, tracers don't increase total
    const result =  traverse(index + 1, total + inputArr[index]) ||
          traverse(index + 1, total)
    cache[key] = result; 
    return result; 
  }
  return traverse(0,0);
}
console.log(equalSizePartition(example1)); 
console.log(equalSizePartition(example2)); 
console.log(equalSizePartition(example3)); 


/*       0 1 2 3 4 5 5 6 7 8
       --------------------
   [] |  1 0 0 0 0 0 0 0 0 0
    1 |  1 0 0 1 0 0 0 0 0 0
    2 |  1 0 1 1 0 1 0 0 0 0 
    1 |  1 1 1 1 1 1 1 0 0 0 
    4 |  1 1 1 1 1 1 1 1 1 1
    5
    1
*/
