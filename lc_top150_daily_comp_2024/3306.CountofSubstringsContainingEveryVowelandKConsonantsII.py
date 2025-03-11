'''
3306. Count of Substrings Containing Every Vowel and K Consonants II
Solved
Medium
Topics
Companies
Hint
You are given a string word and a non-negative integer k.

Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

 

Example 1:

Input: word = "aeioqq", k = 1

Output: 0

Explanation:

There is no substring with every vowel.

Example 2:

Input: word = "aeiou", k = 0

Output: 1

Explanation:

The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:

Input: word = "ieaouqqieaouqq", k = 1

Output: 3

Explanation:

The substrings with every vowel and one consonant are:

word[0..5], which is "ieaouq".
word[6..11], which is "qieaou".
word[7..12], which is "ieaouq".
 

Constraints:

5 <= word.length <= 2 * 105
word consists only of lowercase English letters.
0 <= k <= word.length - 5
'''

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        N, start, left, ans = len(word), 0, 0, 0

        # map 'aeiou' to be 0,1,2,3,4, respectively and consonants are mapped to 5
        word = list(map(lambda x: 'aeiou'.index(x) if x in 'aeiou' else 5, word))
        # print(word)

        char_cnt = [0, 0, 0, 0, 0, 0]

        for right in range(N):
            char_cnt[word[right]] += 1

            while left < right and char_cnt[5] > k:
                idx = word[left]
                char_cnt[idx] -= 1
                left += 1
                start = left
            
            while char_cnt[5] == k and left < right:
                idx = word[left]
                if idx < 5:
                    if char_cnt[idx] > 1:
                        char_cnt[idx] -= 1
                        left += 1
                    else:
                        break
                else:
                    break
            
            if char_cnt[5] == k and min(char_cnt[:5]) > 0:
                ans += (left - start + 1)
        
        return ans