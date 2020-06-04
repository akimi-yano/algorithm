// # 560. Subarray Sum Equals K
// # https://leetcode.com/problems/subarray-sum-equals-k/

// # Medium

// # 4354

// # 138

// # Add to List

// # Share
// # Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

// # Example 1:

// # Input:nums = [1,1,1], k = 2
// # Output: 2
 

// # Constraints:

// # The length of the array is in range [1, 20,000].
// # The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

// Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

// Example 1:

// Input:nums = [1,1,1], k = 2
// Output: 2
// 2- sliding window
// 3 - Prefix sum 
// ———
// [1,5,5,10,10,5] k = 20
//                   |   |

// sum = 1+5+5+10

// sum > k
//     sum-=arr[start]
// 	start ++
// sum <  k
//    sum+=arr[end]
// 	end++

// sum == k: 
// 	count ++
//     sum-=arr[start]
// 	sum+=arr[end]
// 	start++
// 	end++

// */

function numK(nums, k){
  let count = 0
  for(let start=0; start<nums.length; start++){
    let sum = 0
    for(let end = start; end <nums.length; end++){
      sum+=nums[end]
      if(sum==k){
        count++
      }
    }
  }
  return count 
}
function numsK(nums, k){
  let sum = 0
  let start = 0
  let end = 0
  let count = 0
  while(end < nums.length){
    if(sum < k){
      sum+=nums[end]
      end++
    } else if (sum > k){
      sum-=nums[start]
      start++
    }else{
      count ++
      sum-=nums[start]
	    sum+=nums[end]
	    start++
	    end++
    }
  }
  return count 
}

console.log(numsK([1,5,5,10,10,20], 20))


