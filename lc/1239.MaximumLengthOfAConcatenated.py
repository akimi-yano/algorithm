# 1239. Maximum Length of a Concatenated String with Unique Characters
# Medium

# 1347

# 131

# Add to List

# Share
# Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

# Return the maximum possible length of s.

 

# Example 1:

# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
# Maximum length is 4.
# Example 2:

# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible solutions are "chaers" and "acters".
# Example 3:

# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
 

# Constraints:

# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lower case English letters.


# This solution works:


'''
This problem is medium, not hard, because given constraints it is possible to do just bruteforce solution: check for every one of 2^16 subsets if concatenation have all different symbols. However we can do better.

First of all, number of letters in alphabet is not big: only 26, so we can use the idea of bitmask: encode every word with number. For example for word dab, we can use mask 1011 (we start from end).

First of all, we take only words with different letters, and remove all others.
Next step is for every word evaluate its mask and also number of letters. We keep tuple. For example d[1<<i] = (1011, 3) for word dab, where i is index of this word. Why we use 1<<i, not just i? You will see it later.
dp(m) is maximum answer we can have if we use bitmask of words indexes m. Notice, it is another bitmask, not what we discussed previously. For example, if we have arr = [ab, cd, ef, gh], then m = 1011 means that we take ab, cd, gh as our solution. dp(m) will return two values: bitmask of used letters and number of used letters.
How we can find dp(m)? If m == 0, we return (0, 0). Next we find the last 1 in our m, usint m & (m-1) trick. Then we check if m_last & d[m - prev][0] != 0. If it is the case, it means that we have some letters repeated, so we return (0, -10000) in this case where -10000 represents minus infinity. In the opposite case we return (m_last | d[m - prev][0], bits_last + d[m - prev][1]), because we need to turn on bits d[m - prev][0] in mask m_last and number of bits is bits_last + d[m - prev][1]. Notice that we can keep in fact only one value and evaluate the second on flight, but it will not be true O(1).
In the end we just check all masks dp(x) and return one with the biggest number of letters on.
Complexity
It is O(2^n) for time and O(2^n) for space.
'''
class Solution:
    def maxLength(self, arr):
        arr = [word for word in arr if len(set(word)) == len(word)]
        
        d = {}
        for i, word in enumerate(arr):
            d[1<<i] = (sum(1<<(ord(w) - 97) for w in word), len(word))

        @lru_cache(None)
        def dp(m):
            if m == 0: return (0, 0)
            prev = m & (m - 1)
            m_last, bits_last = dp(prev)
            if m_last & d[m - prev][0] != 0: return (0, -10000)
            return (m_last | d[m - prev][0], bits_last + d[m - prev][1])
        
        return max(dp(x)[1] for x in range(1<<len(arr)))