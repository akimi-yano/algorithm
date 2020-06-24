// '''
// let input = [1,3,5,7,9] - can have negatives and 0s 
//              0 1 2 3 4
// #  input take an array specified above
// //  output = [745, 315, **, 105,  ]
//               0[3*5*7*9] 1[1*5*7*9]
// // 1963      
// Time - O(N)
// Space - O(N)

// easy way 
// with constrain
// '''

// # [1, 3, 5, 7, 9]
// # [0][1][2][3][4]
// # sub = arr[:i]+arr[i+1:]

// #  i = 0 sub = arr[:i]+arr[i+1:]
// #  i = 1 sub = arr[:i]+arr[i+1:]
// #  i = 2
// #  i = 3
// #  i = 4
 
// # ans = []
// # temp = 1
// # iterate through sub


// # def multiply_rest(arr):
// #     ans = []
// #     for i in range(len(arr)):
// #       sub = arr[:i]+arr[i+1:]
// #       temp = 1
// #       for num in sub:
// #         temp*=num
// #       ans.append(temp)
// #     return ans
// # print(multiply_rest([1,3,5,7,9])) 


// # [1,3,5,7,9]
// # except 1 - 3*5*7*9 


// cons1: it can take any integer numbers including negative values
// cons2: it should have time complexity of o(N)
// cons3: it should have auxillary space complexity of o(N)
// cons4: dont use divide

// Solution -1 : easy 
// I will multiply all the elements of the array and store it 
// in variable totalSum;
//I will declare target array
// iterate over source array, for each element i will push target array element totalSum/arr[i]
//target array = [945/1, 945/3, 945/5, 945/7, 945/9]

function multiplyExceptSelfIndex(arr) {
  
  let totalSum = 1;
  let tgtArray = [];
  
  for(let i=0; i< arr.length; i++) {
    totalSum *= arr[i];
  }
  
  for(let j=0; j<arr.length; j++) {
    tgtArray.push(totalSum/arr[j]);
  }
  
  return tgtArray;
}

console.log(multiplyExceptSelfIndex([1,3,5,7,9]))








