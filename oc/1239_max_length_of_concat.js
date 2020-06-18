// 1239. Maximum Length of a Concatenated String with Unique Characters
var maxLength = function(arr) {
  let len = 0
  
  function helper(i, str){
      
      if(str.length!= new Set(str.split('')).size) 
          return 
      
      len = Math.max(len, str.length)
      
      for(let j = i; j<arr.length; j++){
          helper(j+1,`${str}${arr[j]}`)
      }
      
  }
    helper(0,'')
    return len
};

//O(n)^2
// M = len the biggest element + callstack

// back track and DP

// test
// a = "abs"
// set_a = new Set(a)
// console.log(set_a)