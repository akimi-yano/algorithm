'''
3003. Maximize the Number of Partitions After Operations
Hard
Topics
premium lock icon
Companies
Hint
You are given a string s and an integer k.

First, you are allowed to change at most one index in s to another lowercase English letter.

After that, do the following partitioning operation until s is empty:

Choose the longest prefix of s containing at most k distinct characters.
Delete the prefix from s and increase the number of partitions by one. The remaining characters (if any) in s maintain their initial order.
Return an integer denoting the maximum number of resulting partitions after the operations by optimally choosing at most one index to change.

 

Example 1:

Input: s = "accca", k = 2

Output: 3

Explanation:

The optimal way is to change s[2] to something other than a and c, for example, b. then it becomes "acbca".

Then we perform the operations:

The longest prefix containing at most 2 distinct characters is "ac", we remove it and s becomes "bca".
Now The longest prefix containing at most 2 distinct characters is "bc", so we remove it and s becomes "a".
Finally, we remove "a" and s becomes empty, so the procedure ends.
Doing the operations, the string is divided into 3 partitions, so the answer is 3.

Example 2:

Input: s = "aabaab", k = 3

Output: 1

Explanation:

Initially s contains 2 distinct characters, so whichever character we change, it will contain at most 3 distinct characters, so the longest prefix with at most 3 distinct characters would always be all of it, therefore the answer is 1.

Example 3:

Input: s = "xxyz", k = 1

Output: 4

Explanation:

The optimal way is to change s[0] or s[1] to something other than characters in s, for example, to change s[0] to w.

Then s becomes "wxyz", which consists of 4 distinct characters, so as k is 1, it will divide into 4 partitions.

 

Constraints:

1 <= s.length <= 104
s consists only of lowercase English letters.
1 <= k <= 26

'''

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        '''
        1) convert every character into bitmask: 
            ex) 'a' -> 1 << 0, 'b' -> 1 << 1
        2) bitmask : current distinct characters in this partition
        3) for each character, choose:
            A) add it to the current partition (if distinct count <= k)
            B) start a new partition (if adding it exceeds k)
        4) if i still have the option to change, try changing the current character to all 26 possibilities and compute the best outcome
        5) helper(0, 1, 0) + 1 <- add 1 because the last segement counts as one partition
        '''
        N = len(s)
        masks = [1 << ord(char) - ord('a') for char in s] 
        # ex) a: 1 , c: 100
        
        @cache
        def helper(i, can_change, mask):
            if i == N:
                return 0
            new_mask = mask | masks[i]
            ans = 0
            # adding it will exceed k, so start a new partition
            if new_mask.bit_count() > k:
                ans = 1 + helper(i+1, can_change, masks[i])
            # adding it will not exceed k, so add it to the current paritition
            else:
                ans = helper(i+1, can_change, new_mask)
            
            if can_change:
                for char_ord in range(26):
                    changed_mask = mask | (1 << char_ord)
                    # start a new partition
                    if changed_mask.bit_count() > k:
                        ans = max(ans, 1+helper(i+1, 0, 1 << char_ord))
                    # add it to the current paritition
                    else:
                        ans = max(ans, helper(i+1, 0, changed_mask))
            return ans

        return helper(0, 1, 0) + 1 # add 1 to count the last segment