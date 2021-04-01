# 936. Stamping The Sequence
# Hard

# 402

# 105

# Add to List

# Share
# You want to form a target string of lowercase letters.

# At the beginning, your sequence is target.length '?' marks.  You also have a stamp of lowercase letters.

# On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.  You can make up to 10 * target.length turns.

# For example, if the initial sequence is "?????", and your stamp is "abc",  then you may make "abc??", "?abc?", "??abc" in the first turn.  (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)

# If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each turn.  If the sequence is not possible to stamp, return an empty array.

# For example, if the sequence is "ababc", and the stamp is "abc", then we could return the answer [0, 2], corresponding to the moves "?????" -> "abc??" -> "ababc".

# Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within 10 * target.length moves.  Any answers specifying more than this number of moves will not be accepted.

 

# Example 1:

# Input: stamp = "abc", target = "ababc"
# Output: [0,2]
# ([1,0,2] would also be accepted as an answer, as well as some other answers.)
# Example 2:

# Input: stamp = "abca", target = "aabcaca"
# Output: [3,0,1]
 

# Note:

# 1 <= stamp.length <= target.length <= 1000
# stamp and target only contain lowercase letters.



# This approach does not work:

# class Solution:
#     def movesToStamp(self, stamp: str, target: str) -> List[int]:
#         ans = ("?" for _ in range(len(target)))
#         last_idx = len(target) - len(stamp)
#         target = list(target)
        
#         @lru_cache(None)
#         def helper(arr):   
#             if arr == target:
#                 return [[]]
            
#             temp = []
#             for start in range(last_idx+1):
#                 newarr = list(arr)
#                 if start in seen:
#                     continue
#                 seen.add(start)
#                 k = 0
#                 for idx in range(start, start+len(stamp)):
#                     newarr[idx] = stamp[k]
#                     k += 1
#                 newtup = tuple(newarr)
#                 temp.extend([start]+ elem for elem in helper(newtup))
#                 seen.remove(start)
#             return temp
        
#         seen = set([])
#         ans = helper(ans) 
#         if not ans:
#             return ans
#         return ans[0]

# This solution works! - DP:

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
        ans = helper(0, float('-inf'))
        if not ans:
            return []
        ans.pop()
        return ans