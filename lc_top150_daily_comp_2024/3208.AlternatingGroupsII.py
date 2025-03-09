'''
3208. Alternating Groups II
Medium
Topics
Companies
Hint
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

Example 1:

Input: colors = [0,1,0,1,0], k = 3

Output: 3

Explanation:



Alternating groups:



Example 2:

Input: colors = [0,1,0,0,1,0,1], k = 6

Output: 2

Explanation:



Alternating groups:



Example 3:

Input: colors = [1,1,0,1], k = 4

Output: 0

Explanation:



 

Constraints:

3 <= colors.length <= 105
0 <= colors[i] <= 1
3 <= k <= colors.length
'''

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        '''
        [0,     1,      0,      1,      0], k >= 3
        
        0: 1    0: 1    0: 2    0: 2    0: 3
        1: 0    1: 1    1: 1    1: 2    1: 2
        
        len of alt 5
        k 3
        options = len of alt - k +1
        if len of alt >= k
        '''
        ans = 0
        len_of_alt = 1
        if colors[0] != colors[-1]:
            colors = colors + colors[:k-1]

        for i in range(1, len(colors)):
            if colors[i-1] != colors[i]:
                len_of_alt += 1
            else:
                if len_of_alt >= k:
                    options = len_of_alt -k +1
                    ans += options
                len_of_alt = 1

        if len_of_alt >= k:
            options = len_of_alt -k +1
            ans += options

        return ans

# Simplified:

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:(k-1)]) # modifies the original list in place
        count = 0
        left = 0

        for right in range(len(colors)):
            
            if right > 0 and colors[right-1] == colors[right]:
                left = right

            if (right - left + 1) >= k:
                count += 1

        return count