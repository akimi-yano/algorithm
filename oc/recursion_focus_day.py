'''
Topic: Recursion
'''



'''
https://codeinterview.io/AFYQRGBWZW	Medium	Arrays & Strings
https://leetcode.com/problems/maximum-average-subarray-ii/	Hard	Arrays & Strings
No specific problem, just general strategy/approach for recursion problems.	Medium	Recursion
https://leetcode.com/problems/break-a-palindrome/	Medium	Arrays & Strings
https://leetcode.com/problems/word-ladder-ii/	Hard	Graphs
https://leetcode.com/discuss/interview-question/479911/GoogleorPhoneorFind-nth-node-in-inorder-traversal	Medium	Trees
https://leetcode.com/problems/allocate-mailboxes/	Hard	Dynamic Programming
'''

'''
https://leetcode.com/problems/subsets/
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3] =[[1]], [[1,2]], [[2,3]], [[3]]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if not nums: return []
        
        def traverse(build, index):
            
            if index == len(nums):
                results.append(build)
                return
                
            traverse(build, index+1)
            traverse(build + [nums[index]], index+1)
        
        results = []
        traverse([], 0)
        return results 


          


         0                 []
         1        /            |              \        
                 1            2                   3 ---> 3 n,
         2      | \           / \     
                1,2 1,3       2,1(remove) 2,3 ---->  
                
                
                
                nums = 1, 2, 3
                          i   j
                             
                             
                                            i   curr res
                                      f(nums, 0, [], [])
                                          /                           \
                            f(num, 1, [], [])                           f(nums, 1, [1], res)
                              /                    \
                  f(nums, 2, [], [])                  f(nums, 2, [2], [[], [3]])
                      /                   \              /                 \
          f(nums, 3, [], [[]])  f(nums, 3, [3], [[]] )  f(nums, 3, [2], res)   f(nums, 3, [2, 3], res)
                  
                  
          result = [[], [3], [2], [2, 3]]
                    
      
                 
                 
'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

17. Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
 could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map
 to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''     

l_dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
                       '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
                       
                       
                              2,3
                        /       |    \ 
                    build =a           b           c
                 /|\          / | \     / | \  
      build=a    + d  e  f      d  e f    d  e   f 

        
        
        


    # Time O(3^N) Space O(3^N), runtime = 28 ms
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits: return []
        
        results = []
        l_dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
                       '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
                       
                       
        k,v k=num, v = string
        
        def combine(index, build):
        
            if len(build) == len(digits):
                results.append(build)
                return
            
            # d = 2
            d = digits[index]
            
            for v in l_dict[d]:
                combine(index+1, build+v)
            
        combine(0,'')
        return results

           01
digits  : "23", index=0
d=2
l_digits: { 2: "abc"}
v = "a" //b
d = 3
l_digits: { 3: "def"}
v = "f"

"a" + "f"


'''
46. Permutations
Medium

4742

115

Add to List

Share
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

#               1, 2, 3
#     i=0           i=1          i=2
#      1             2            3
#   i=1  i=2      i=1  i=2    i=1  i=2
#   12   13        21   23     31   32
#   i=2  i=1      i=2  i=0    i=1  i=0
#   123  132      213  231    312  321
    
    # Time O(N!) Space O(N!)
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def mutation(build, lst):
        
            if len(build) == len(nums):
                results.append(build)
                return
            
            for i in range(len(lst)):
                mutation(build + [lst[i]], lst[:i] + lst[i+1:])
             
        results = []
        mutation([], nums)
        return results
                 




