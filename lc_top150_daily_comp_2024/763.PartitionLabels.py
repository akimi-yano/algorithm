'''
763. Partition Labels
Medium
Topics
Companies
Hint
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_counts = Counter(s)
        ans = []
        left = 0
        cur = Counter()
        for right in range(len(s)):
            char = s[right]
            cur[char] += 1

            for k, v in cur.items():
                if v < char_counts[k]:
                    break
            else:
                ans.append(right - left + 1)
                left = right + 1
        return ans

# Another approach / optimization:

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        N = len(s)
        last = {s[i]: i for i in range(N)} # char: index of the char's last apparence
        start = 0
        ans = []
        while start < N:
            char = s[start]
            end = last[char]
            inbetween_i = start + 1
            while inbetween_i < end: # extend the end if I see any char that has larger end
                inbetween_char = s[inbetween_i]
                if last[inbetween_char] > end:
                    end = last[inbetween_char] 
                inbetween_i += 1
            ans.append(end - start + 1) 
            start = end + 1
        return ans