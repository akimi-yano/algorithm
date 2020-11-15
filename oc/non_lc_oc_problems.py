




# Given a list of numbers, find all the minimum peaks in the list using the following operation.
# Each time you find a peak, delete it and store it to be returned at the end.
# Examples:
# [1,4,5,3,8,6] , output = [5,4,8,6,3,1]
# [1,4,5,3,8,6], Min peak = 5, resultant = [1,4,3,8,6]
# [1,4,3,8,6], Min peak = 4, resultant = [1,3,8,6]
# [1,3,8,6], Min peak = 8, resultant = [1,3,6]
# [1,3,6], Min peak = 6, resultant = [1,3]
# [1,3], Min peak = 3, resultant = [1]
# [1], min peak = 1
# Output = [5,4,8,6,3,1]

"""
class Solution {
  public static List<Integer> minimumPeaks(int[] nums) {
    PriorityQueue<Integer> maxHeap = new PriorityQueue<>(nums.length, Collections.reverseOrder());
    List<Integer> result = new ArrayList<>();
    
    for (int num : nums) {
      while (!maxHeap.isEmpty() && num < maxHeap.peek()) {
        result.add(maxHeap.remove());
      }
      //if there is any remaining numbers within max heap, pop from heap and add into the result
      if (maxHeap.isEmpty() || num > maxHeap.peek()) {
        maxHeap.add(num);
      }
    }
    
    while (!maxHeap.isEmpty()) {
      result.add(maxHeap.remove());
    }
    return result;
  }
}"""
# ---------------------------------
from heapq import heapify

def minimal_peak(arr):
  heap = []
  heapq._heapify_max(heap)
  result = []
  
  for i in range(len(arr)):
    nums = arr[i]
    while not heap and nums < heapq._heapify_max(heap):
      max_from_heap = heapq._heappop_max(heap)
      result.append(max_from_heap)
      
    if not heap or nums>max_from_heap:
      heap.push(nums)
      
  while heap:
    result.append(max_from_heap)
  
  return result
arr = [1,4,5,3,8,6]
print(minimal_peak(arr))
    
  
  
      
    
    
  
  
  
minimal_peak(self, arr)




#Rotate a matrix in clockwise direction without any extra space.
#You can't rotate the numbers on the diagonals.
# Driver code
A = [[1, 2, 3, 4],  
     [5, 6, 7, 8], 
     [9, 10, 11, 12], 
     [13, 14, 15, 16]]  
   
'''
def rotate(m):
  N = len(m)
  for sub_matrix in (floor(m/2)):
    for j in range(j-sub_matrix-1):
      temp = m[sub_matrix][j]
      rightcor = m[]
'''


#Give a number, output the difference between the sum
#of all digits and the product of all digits.
#For example: input 1, 2, 3, output: 0 Explanation: 1 * 2 * 3-(1 + 2 + 3) =0

def product_sum(n):
  sums = 0
  prod = 1
  while n:
    n, remainder = divmod(n, 10)
    sums += remainder
    prod *= remainder
  
  return prod - sums
    
    
  product_sum(remain)

# print(product_sum(10))


# 1 solution.
def palind(st):
  def is_palindrome(subs):
    return subs == subs[::-1]
  
  for i in range(len(st)-1,1,-1):
    if is_palindrome(st[:i+1]):
      print(f"{st[:i+1]} is a palindrome")
      print(f"call palindrome for new str = {st[i+1:]}")
      return palind(st[i+1:])
      
  return st

  
print("1/3 solution, func delcared in line 2")
print(palind("aaaabcbddfd"))

#2/3 solution
def find_longest(s):
    if len(s) <= 2: return s
    max_pal = ''
    n = len(s)
                    
    while n > 2:
    # left half       str [reversed][the left half] because we reversed it actually is right half
      if s[:n//2] == s[:n][::-1][:n//2]:
       
          break
      i -= 1
    return find_longest(s[i:])
# print(find_longest("cacbac" )) # 'd'


#3rd solution   
def prefix_palindrome(st):
  
  def palindrome(s, i):
    subslic = st[s:i+1]
    return subslic == subslic[::-1]
  
  s = 0
  i = len(st) - 1
  while True:
    if i - s < 2:
      # We've gotten to the smallest it can be without finding a palindrome
      print("Returning: ", st[s:])
      return st[s:]
    elif palindrome(s,i):
      print(f"{st[s:i+1]} is a palindrome")
      s = i+1
      i = len(st)-1
      flag = True
    else:
      print(f"{st[s:i+1]} isn't a palindrome, i is now {i-1}")
      flag = False
      # Not a palindrome, try one smaller
      i -= 1
  
  return st[s:]
# print("3rd solution-line 31 : ")
# print(prefix_palindrome("banananab"))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# for two arrays, a lower bound, an upper bound, calculate how many pair,
#  to meet lower <= a [i] ** 2 + b[i] ** 2 <= upper 
# example: input: a = [2, 3], b = [3, 4], upper bound = 18, lower bound = 10
# output: 2
# Explanation:
# 2 * 2 + 3 * 3 = 13 (satisfy the conditions)
# 2 * 2 + 4 * 4 = 20 (The conditions are not met)
# 3 * 3 + 3 * 3 = 18 (The conditions are met
# 3 * 3 + 4 * 4 = 26 (The conditions are not met)

a = [2, 3]
b = [3, 4]
upper = 18
lower = 10
def matrix_mul(a,b,lower,upper):
  a = sorted(a)
  b = sorted(b)
  count = 0
  for i in a:
    for j in b:
      total = i**2+j**2 
      print(total)
      if i**2+j**2 <= upper and i**2+j**2 >= lower:
        
        count += 1
  return count

# print(matrix_mul(a,b,lower,upper))



msg = """Lorem ipsum dolor sit amet,consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse 
dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
 non proident, sunt in culpa qui officia deserunt mollit anim 
 id est laborum."""
 
output = """ ['Lorem ipsum dolor sit amet,consectetur adipiscing elit,
  sed do eiusmod tempor incididunt ut labore et dolore magna 
  aliqua. Ut enim ad minim veniam, quis (1/3)', 'nostrud 
  exercitation ullamco laboris nisi ut aliquip ex ea commodo
  consequat. Duis aute irure dolor in reprehenderit in
  voluptate velit esse dolore eu (2/3)',
  'fugiat nulla pariatur. Excepteur sint occaecat 
  cupidatat non proident, sunt in culpa qui officia 
  deserunt mollit anim id est laborum. (3/3)']"""
                   
msg2 = "To be, thought his question: who would fard the ill, must give \
under a weat pause. \
Ther whips and man's coward that undiscorns tural country from whether"

output2 = """To be, thought his question: who would fard the ill, must 
give under a weat pause. Ther whips and man's 
coward that undiscorns tural country from whether"""

#write a function that taxts to be sent and splits it in into different
# text segements. every text segment should have suffixes that specify
# the text number.
#the # of segments is not going 9.

 #1 
# 500
# max = 160 * 4 =  640(valid) 4  +1 
#     = 160 * 10 = 16 + 5 (invalid)

# n = 160   
# len = 437 / 160 = ~2.7 ~~ 3

# 437 + (3*5) = 452 / 160 = 2.8 =~ 3
# 3 * 5 = 15
# suffix = (1/2) 
# "today is monday", "tomorrow", "is"
# "today", "is", "monday"
#   0        1     2    3

  
# (1/100) 
# (2/100) 
# .....
# (1/9)

#
    
def ms(text, n):
  if len(text) <= n:
    return text
  subtext = " "
  result = []
  words = text.split()
  for index, word in enumerate(words):
    if len(subtext) + len(word) <= n-6:
      subtext += word+ " "
    else:
      result.append(subtext)
      subtext = word+" "
  if len(subtext) > 0:
    result.append(subtext)
    
  return [f"{text} ({i+1}/{len(result)})" for i, text in enumerate (result)]

#print(ms(msg,160))






# Company: FB
# When you know what language you would like to use for your interview,
# simply choose it from the dropdown in the top bar.
# Enjoy your interview!
# Given a bread with strawberries on it, figure out if we can cut the#
#bread n times and make all the pieces have exact same number of strawberries
# Example
# def bread_cut(n, bread):
# Input-1: integer n #times cut the bread.
# Input-2: bread= [true, false, true, false, true] where true represents\ that there is a strawberry, and vise versa.
# Output: if n=2, return true. If n!=2, return false
# [false, true, false] n = 2 # cuts, not # of pieces. return false.
#        |    |

# ["True", "False", True, False, True]  n = 2 returns True (3 -total of trues-  % n+1 == 0)
#         |              |


# ["True", "False", True, False, False, False]  n = 2 returns False
# total number of trues, mod by (n+1) == 0 ? true : false
# bread = ["T","F","T","T","T"] 
# n = 2

# ['T', 'T', 'T', 'T'] n=1, False
          # | 

from typing import List

def strawberry(arr, n):
  if n < 0: return False
  
  total = 0
  for i in arr:  
    if i == "T":
      total+=1
    
  if total % (n+1) ==0:
    return True
  else:
    return False
  
# print(strawberry(bread,n))


# [5,5,0,0,10,10]   30 mod 3 = 0 return True
#         |  |
# [20,0,0,1,0 9] return False

# n = 2   return True
# slice = 3
#totalSum / n + 1  (30 % 3 == 0 ? yes) (30/3 = 10-sliceSum)

# runningSum == sliceSum (20 >= 10)
    # runningSum = 0
    # slice--
# return slice == 0
arr = [20,5,0,0,10,10]
n = 2
def strawberry_number(arr, n):
  totalSum = sum(arr)
  
  if totalSum%(n+1) != 0:
    return False
    
  strawberry_per_slice = totalSum//(n+1) 
  runningSum = 0
  for i in arr:
    runningSum += i
    if runningSum == strawberry_per_slice:
      #make slice
      n-=1
      runningSum = 0
      
  if n == -1:
    return True
  else:
    return False
    
#print(strawberry_number(arr, n))
    
    
    # (30 % 3 == 0 ?
    
    
  

  


# |      10    |   10  |   10  |


# 10, 10, 10   30   n = 2


# count # of t. 3  and n=2 if  #ts = n+1 return true else return false. 
# [t,t,  t,t,f] = 1   ts= 4  =    2+1  
# 10 I  10  LEFT = RIGHT
# 10,  10,  10  T   30   n =2 30/N+1 = 10

# 10, 9, 10,    Ts  29   N= 2 29 /N+1 = 9.3
# 10,8,8  = 26/3 = 8.5

'''
#763. Partition Labels
class Solution:
    def partitionLabels(self, S: str) -> List[int]:        
        if S is None or len(S) == 0: return []
        lstlast = []        
        d = {}
        
        # loop once and build dictionary with list of indexes of each char
        for i in range(len(S)):
            if S[i] in d: d[S[i]].append(i)
            else: d[S[i]] = [i]
        #print(d)
        # {'a': [0, 2, 6, 8], 'b': [1, 3, 5], 'c': [4, 7], 'd': [9, 14], 'e': [10, 12, 15], 'f': [11], 'g': [13], 'h': [16, 19], 'i': [17, 22], 'j': [18, 23], 'k': [20], 'l': [21]}
        
        s = set()
        max = -1
        premax = 0
        for i in range(len(S)):
            ch = S[i]
            lst = d[ch]
            eachidx = lst[len(lst)-1]
            if max != 0 and i == max:
                lstlast.append(i+1 - premax)
                #max = 0
                premax = i + 1
            elif max < eachidx: 
                max = eachidx
                if i == max:
                    lstlast.append(1)
                    premax = i + 1            
            #print(f"{ch}, {i}, max: {max}, premax: {premax}, eachidx: {eachidx}, lstlast: {lstlast}")
                                
        return lstlast
'''






#A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

#Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

#We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

#Example 1:
#Input: 
#["9001 discuss.leetcode.com"]
#Output: 
#["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
#Explanation: 
#We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.

subdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
#output = ["901 mail.com","50 yahoo.com","900 google.mail.com",
#"5 wiki.org","5 org","1 intel.mail.com","951 com"]

                   
def count_paired_domain(subd):
    result = []
    counts = {}
    while len(subd) > 0:
        count_str = subd.pop()
        count_str = count_str.split()
        
        domain = count_str.pop()
        count = int(count_str.pop())
        
        for i in range(len(domain) - 1, -1, -1):
            char = domain[i]
            if char == "." or i == 0:
                if domain[i:] in counts:
                    counts[domain[i:]] += count
                else:
                    counts[domain[i:]] = count
                    
    for key in counts:
        result.append(f"{counts[key]} {key}")
        
    return result
    
#print(count_paired_domain(subdomains))



################################
# RECURSIVE PLUS ONE LINKED LIST
# Time Complexity: O(N)
# Space Complexity: O(N)
# @danrneal
################################
def plus_one(head):
    cur = head
    def add_one(node):
        if node.next is None:
            node.value += 1
            if node.value == 10:
                node.value = 0
                return 1
            
            return 0
            
        node.value += add_one(node)
        if node.value == 10:
            node.value = 0
            return 1
            
        return 0
        
    carry = add_one(head)
    if carry == 1:
        new_head = Node(1)
        new_head.next = head
        head = new_head
        
    return head


################################
# ITERATIVE PLUS ONE LINKED LIST
# Time Complexity: O(N)
# Space Complexity: O(N)
# @danrneal
################################
def plus_one(head):
    stack = []
    current = head
    while current is not None:
        stack.append(current)
        current = current.next
        
    carry = 1
    while len(stack) > 0:
        current = stack.pop()
        if carry == 1:
            current.value += 1
            if current.value == 10:
                current.value = 0
            else:
                carry = 0
                
    if carry == 1:
        new_head = Node(1)
        new_head.next = head
        head = new_head
        
    return head


# Win/Loss Rounds
# Given a number of rounds in a game, return every permutation of wins and losses that may occur.
# There will be no ties.
# The output should be an array of strings. A win will be represented with the letter X and a loss will be represented with the letter O.
# Example input 1: 3
# output: ['XXX', 'XXO', 'XOX', 'OXX', 'XOO', 'OXO', 'OOX', 'OOO']

# Example input 2: 2
# output: []



# [5, 4, 1, 3, 4]  2
# In the above the first team has 5 developers , second 4 developers and so on.
# You are also given an integer newHire representing how many more developers
#  you have the budget to hire. Your goal is to hire in such a way that maximizes 
# the number of teams having equal developers.
#  For example if newHire = 2. You have two options:
# (1) Hire 1 developer for the forth team ( index == 3 ). 
# Do not do further hiring. The teams array will become :
# [5, 4, 1, 4, 4]
# (2) Hire 1 developer for the first team and 1 developer
#  for the 5th team. The teams array will become:
# [5, 5, 1, ,3, 5]
# The output should be the numbers of teams having equal number
#  of developers when the above hiring scheme is used. 
# In the above example the expected output is 3.








# // # 2520 is the smallest number that can be divided by each of 
# // # the numbers from 1 to 10 without any remainder.

# // # What is the smallest positive number that is evenly
# // #  divisible by all of the numbers from 1 to 20?
# other approches, prime factorization, and doubling elements from 1->10, 7*7 = 14,
# dont calcuate for 12,14,16,18. 
# // def divisible(num):
# //   for i in range (1, 21):
# //     if num % i != 0:
# //       return True 
# //   return False

# // def multiple(num):
# //   i = 2520 
# //    #=>  3 20 = 60
# //   while (divisible(i) == True):
# //     i+=60
  
# //   return i
# // num = 0
# // print(multiple(num))
  
  

# needs to be completed. @@@@@@@@@@@
# Write a program to reverse a stack using recursion. 
# You are not allowed to use loop constructs like while, for..etc, 
# and you can only use the following ADT functions on Stack S:
# isEmpty(S)
# push(S)
# pop(S)


# #Function to Reverse:
# def reverse(stack):
#   if not isEmpty(stack):
#     temp = stack.pop()
#     #recursive call
#     reverse(stack)
#     #second recursive call to push element at bottom
#     push(stack) 
    
# Function to check if  
# the stack is empty 
def isEmpty( stack ): 
    return len(stack) == 0
  
# Function to push an  
# item to stack 
def push( stack, item ): 
    stack.append( item ) 
  
# Function to pop an  
# item from stack 
def pop( stack ): 
  
    # If stack is empty 
    # then error 
    if(isEmpty( stack )): 
        print("Stack Underflow ") 
        exit(1) 
  
    return stack.pop() 
    
    





#647 Leetcode Palindromic Substring. 

# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes 
# are counted as different substrings even they consist of same characters.

# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:

# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


s = "abba"
def longestPalindrom(s):
  #Transform S into new string with special characters inserted
  # to account for when the len of string is even and you have two centers
  #acca  --> #a#c#c#a# when it is an even sub string 
  # palindrom, then is the center will be a '#'. 
  #or the palindrom is a even length. 
  HashedS = '#'.join('#{}#'.format(s))

  # arr for size of each palindrom on each index.
  n = len(HashedS)
  P = [0] * n
  # right and center pointers to account for the range of Palindrom
  center = right = 0

  for i in range(1,n-1):
    
    #l---c---r
    #a#c # c#a# 
    #  i   i'
    # if within right range then calucuate i'
    if right > i:
      P[i] = min(right - i, P[2*center - i]) 
    
    # check if the i center can be expanded.
    while i - 1 -P[i] >= 0 and i + 1 + P[i] < n and \
    HashedS[i + 1 + P[i]] == HashedS[i - 1 - P[i]]:
                P[i] += 1

    # If palindrome centered at i expand past right range,
    # adjust center based on expanded palindrome.
    if i + P[i] >= right:
      center, right = i, i + P[i]

  # Find the maximum element in P.
  maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
  return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
  
    
# print(longestPalindrom(s)) 
    
    
# STRING COMPRESSION,
def compress(chars) -> int:
  start = 0 
  res = 0
  # using three pointers, char, res, start..one marks the begining of new char, 
  # start increments to the end and res modifies the arr with char and num of occurance.
  while start < len(chars):
      char  = chars[start]
      count = 0 
      while start < len(chars) and chars[start] == char:
          start += 1 
          count += 1 
      chars[res], res = char, res+1   
      if count > 1:
#         for when count >9 add each num as seperate element in arr.
          for num in str(count):
              chars[res] = num
              res += 1
# number of compressed elements +1 (total index+1 of modified array)
  return res



        