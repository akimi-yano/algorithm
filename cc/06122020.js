// 1. Counting Pairs
// Given an integer k and a list of integers, count the number of distinct valid pairs of integers (a, b) in the list for 
// which a + k = b. Two pairs of integers (a, b) and (c, d) are considered distinct if at least one element of (a, b) does 
// not also belong to (c, d).

// Example
// n = 4
// numbers = [1, 1, 1, 2]
// k = 1
// This array has two different valid pairs: (1, 1) and (1, 2). For k = 1, there is only 1 valid pair which satisfies a + k = b: 
// the pair (a, b) = (1, 2).



// Function Description 
// Complete the function countPairs in the editor below.
// countPairs has the following parameter(s):

//     int numbers[n]:  array of integers
//     int k: target difference

// Returns

//     int: number of valid (a, b) pairs in the numbers array that have a difference of k


// Constraints

// 2 ≤ n ≤ 2 × 105
// 0 ≤ numbers[i] ≤ 109, where 0 ≤ i < n
// 0 ≤ k ≤ 109


// Input Format for Custom Testing
// Sample Case 0
// Sample Input 0

// STDIN     Function 
// -----     ---------
// 6      →  numbers[] size n = 6 
// 1      →  numbers[] = [ 1, 1, 2, 2, 3, 3]
// 1                      
// 2                       
// 2                       
// 3                      
// 3                       
// 1      →  k = 1
// Sample Output 0

// 2
// Explanation 0

// There are 2 valid pairs in numbers = [1, 1, 2, 2, 3, 3] for k = 1, a + 1 = b:

// (1, 2)
// (2, 3)
// Sample Case 1
// Sample Case 2
// Java 8
// Autocomplete Ready



// class Result {


//      * Complete the 'countPairs' function below.
//      *
//      * The function is expected to return an INTEGER.
//      * The function accepts following parameters:
//      *  1. INTEGER_ARRAY numbers

// dont do this, this doesnt work

// function countPairs(numbers, k) {
//     var check = new Set([])
//     var counter = 0
//     for (let i=0;i<numbers.length;i++){
//         check.add(numbers[i])
//     }
//     check.forEach(elem => {
//         if (check.has(elem+k)) {
//             counter++
//         }
//     })
//     return counter

// }

// console.log(countPairs([1, 1, 2, 2, 3, 3],1))
// this code above does not handle the case below
// console.log(countPairs([1,2,3],0))


function countPairs2(numbers, k) {
    var check = {}
    var counter = 0
    for (let i=0;i<numbers.length;i++){
        if (check[numbers[i]+k]){
            check[numbers[i]+k]+=1
        }
        else{
            check[numbers[i]+k]=1
        }
    }
    // console.log(check)
    numbers.forEach(elem => {
        if (elem in check) {
            check[elem]-=1;
            if (check[elem]<1){
                delete check[elem];
            }
            else{
                counter++;
            }
        }
    })
    // console.log(check)
    return counter

}

console.log(countPairs2([1, 1, 2, 2, 3, 3],1))
console.log(countPairs2([1,2,3],0))
console.log(countPairs2([1,1,2,3],0))
console.log(countPairs2([1, 1, 1, 2],1))

// 2. Divisibility Of Strings
// As an assignment, a student is given two strings s and t. Create a function that performs per the following rules.

// Find whether string s is divisible by string t.  A string s divisible by string t if string t can be concatenated some number of times to obtain the string s.
// If s is divisible, find the smallest string u such that it can be concatenated some number of times to obtain both s and t.
// If it is not divisible, set the return value to -1.
// Finally, return the length of the string u or -1.

// Example 1:

// s = "bcdbcdbcdbcd"

// t = "bcdbcd"


// If string t is concatenated twice, the result is "bcdbcdbcdbcd" which is equal to the string s.  The string s is divisible by string t. 

// Since it passes the first test, look for the smallest string u that can be concatenated to create both strings s and t.

// The string "bcd" is the smallest string that can be concatenated to create both strings s and t. 

// The length of the string u is 3, the integer value to return.



// Example 2:

// s = "bcdbcdbcd"

// t = "bcdbcd"



// If string t is concatenated twice, the result is "bcdbcdbcdbcd" which is greater than string s.  
// There is an extra "bcd" in the concatenated string.

// The string s is not divisible by string t, so return -1.



// Function Description 

// Complete the function findSmallestDivisor in the editor below. The function should return a single integer 
// denoting the length of the smallest string u if string s is divisible by string t, or return -1 if not.

// findSmallestDivisor has the following parameter(s):

//    string s : a string

//    string t : a string

// Constraints

// 1 ≤ size of s ≤ 2 x 105
// 1 ≤ size of t ≤  2 x105
//  size of t  ≤ size of s


// Input Format Format for Custom Testing
// Sample Case 0
// Sample Input

// STDIN        Function
// -----        --------
// lrbblrbb  →  s = 'lrbblrbb'
// lrbb      →  t = 'lrbb'
// Sample Output


// 4
// Explanation

// If string "lrbb" is concatenated 2 times the result is string s, so the string is divisible. If string "lrbb" is concatenated 1 time the result is string t. The smallest string that can be concatenated some number of times to get both s and t is "lrbb" with a length of 4.

// Sample Case 1
// Java 8
// Autocomplete Ready



    
    //  * Complete the 'findSmallestDivisor' function below.
    //  * The function is expected to return an INTEGER.
    //  * The function accepts following parameters:
    //  *  1. STRING s


function findSmallestDivisor(s, t) {
    if (s.length % t.length != 0){
        return -1
    }
    let start = 0
    while (start<s.length){
        if (s.substring(start, start+t.length) != t) {
            return -1
        }
        start += t.length
    }
    for (let size=1; size <= t.length; size++) {
        if (t.length % size != 0) {
            continue
        }
        let smaller = t.substring(0, size)
        let start = size
        while (start < t.length) {
            if (t.substring(start, start+size) != smaller) {
                break
            }
            start += size
        }
        if (start >= t.length) {
            return size
        }
    }
    return t.length
}
// console.log(findSmallestDivisor('lrbblrbb','lrbb'))
