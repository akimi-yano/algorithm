# 763. Partition Labels
# Medium

# 6722

# 257

# Add to List

# Share
# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

 

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
# Example 2:

# Input: s = "eccbbbbdec"
# Output: [10]
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.


# This solution works:


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        [(0, 8), (1, 5), (4, 7), 
        0-8
        (9, 14), (10, 15), (11, 11), (13, 13), 
        9-15
        (16, 19), (17, 22), (18, 23), (20, 20), (21, 21)]
        16-23
        '''
        memo = {}
        for i, char in enumerate(s):
            if char not in memo:
                memo[char] = i, i
            else:
                MIN, MAX = memo[char]
                MIN = min(MIN, i)
                MAX = max(MAX, i)
                memo[char] = MIN, MAX
        arr = sorted(memo.values())
        MIN, MAX = arr[0]
        ans = []
        for s, e in arr[1:]:
            if e > MAX:
                if s > MAX:
                    ans.append((MIN, MAX))
                    MIN = s
                    MAX = e     
                else:
                    MIN = min(MIN, s)
                    MAX = max(MAX, e)
        ans.append((MIN, MAX))        
        return [e-s+1 for s, e in ans]
                