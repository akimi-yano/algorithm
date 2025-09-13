'''
3541. Find Most Frequent Vowel and Consonant
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given a string s consisting of lowercase English letters ('a' to 'z').

Your task is to:

Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
Find the consonant (all other letters excluding vowels) with the maximum frequency.
Return the sum of the two frequencies.

Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.

The frequency of a letter x is the number of times it occurs in the string.
 

Example 1:

Input: s = "successes"

Output: 6

Explanation:

The vowels are: 'u' (frequency 1), 'e' (frequency 2). The maximum frequency is 2.
The consonants are: 's' (frequency 4), 'c' (frequency 2). The maximum frequency is 4.
The output is 2 + 4 = 6.
Example 2:

Input: s = "aeiaeia"

Output: 3

Explanation:

The vowels are: 'a' (frequency 3), 'e' ( frequency 2), 'i' (frequency 2). The maximum frequency is 3.
There are no consonants in s. Hence, maximum consonant frequency = 0.
The output is 3 + 0 = 3.
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters only.
'''

class Solution:
    def maxFreqSum(self, s: str) -> int:
        v_count = Counter()
        c_count = Counter()
        for x in s:
            if x in 'aeiou':
                v_count[x] += 1
            else:
                c_count[x] += 1

        max_v_count = max_c_count = 0
        c_count_arr = c_count.values()
        v_count_arr = v_count.values()
        
        if c_count_arr:
            max_c_count = max(c_count_arr) 
        if v_count_arr:
            max_v_count = max(v_count_arr)

        return max_v_count + max_c_count