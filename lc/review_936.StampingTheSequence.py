# <!-- 936. Stamping The Sequence
# Hard

# 758

# 141

# Add to List

# Share
# You are given two strings stamp and target. Initially, there is a string s of length target.length with all s[i] == '?'.

# In one turn, you can place stamp over s and replace every letter in the s with the corresponding letter from stamp.

# For example, if stamp = "abc" and target = "abcba", then s is "?????" initially. In one turn you can:
# place stamp at index 0 of s to obtain "abc??",
# place stamp at index 1 of s to obtain "?abc?", or
# place stamp at index 2 of s to obtain "??abc".
# Note that stamp must be fully contained in the boundaries of s in order to stamp (i.e., you cannot place stamp at index 3 of s).
# We want to convert s to target using at most 10 * target.length turns.

# Return an array of the index of the left-most letter being stamped at each turn. If we cannot obtain target from s within 10 * target.length turns, return an empty array.

 

# Example 1:

# Input: stamp = "abc", target = "ababc"
# Output: [0,2]
# Explanation: Initially s = "?????".
# - Place stamp at index 0 to get "abc??".
# - Place stamp at index 2 to get "ababc".
# [1,0,2] would also be accepted as an answer, as well as some other answers.
# Example 2:

# Input: stamp = "abca", target = "aabcaca"
# Output: [3,0,1]
# Explanation: Initially s = "???????".
# - Place stamp at index 3 to get "???abca".
# - Place stamp at index 0 to get "abcabca".
# - Place stamp at index 1 to get "aabcaca".
 

# Constraints:

# 1 <= stamp.length <= target.length <= 1000
# stamp and target consist of lowercase English letters. -->


# This solution works:


class Solution:
    '''
    stamp = "abc"
    target = "abcbc"
    
    "?????"
    
    "??abc"
       ---

    "abcbc"
     ---
    '''
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        @lru_cache(None)
        def helper(i, prev_start):
            nonlocal stamp, target
            if i >= len(target):
                if prev_start != len(target) - len(stamp):
                    return []
                return [prev_start]
            
            # if we finished processing the stamp that started from prev_start
            if i >= prev_start + len(stamp):
                for offset in range(len(stamp)):
                    if i - offset >= 0 and stamp[offset] == target[i]:
                        subans = helper(i+1, i-offset)
                        if subans:
                            return subans + [prev_start]
                return []
            # else, we are still in the middle of processing the stamp
            else:
                if stamp[i-prev_start] == target[i]:
                    subans = helper(i+1, prev_start)
                    if subans:
                        return subans
                if stamp[0] == target[i]:
                    subans = helper(i+1, i)
                    if subans:
                        return [prev_start] + subans
                return []
        
        if stamp[0] != target[0]:
            return []
        ans = helper(1, 0)
        if not ans:
            return []
        return ans