# 838. Push Dominoes
# Medium

# 2123

# 139

# Add to List

# Share
# There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

# After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

# You are given a string dominoes representing the initial state where:

# dominoes[i] = 'L', if the ith domino has been pushed to the left,
# dominoes[i] = 'R', if the ith domino has been pushed to the right, and
# dominoes[i] = '.', if the ith domino has not been pushed.
# Return a string representing the final state.

 

# Example 1:

# Input: dominoes = "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second domino.
# Example 2:


# Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
 

# Constraints:

# n == dominoes.length
# 1 <= n <= 105
# dominoes[i] is either 'L', 'R', or '.'.


# This solution works:


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ans = list(dominoes)

        lefts = []
        rights = []
        
        for i, elem in enumerate(dominoes):
            if elem == 'L':
                lefts.append(i)
            elif elem == 'R':
                rights.append(i)
        
        while lefts or rights:
            new_lefts = []
            new_rights = []
            
            # R..L
            # R.LL (wrong)
            # RRLL
            for idx in lefts:
                if idx > 0 and ans[idx-1] == '.':
                    if idx > 1 and ans[idx-2] == 'R':
                        continue
                    new_lefts.append(idx-1)

            for idx in rights:
                if idx < len(ans) - 1 and ans[idx+1] == '.':
                    if idx < len(ans) - 2 and ans[idx+2] == 'L':
                        continue
                    new_rights.append(idx+1)
            
            for idx in new_lefts:
                ans[idx] = 'L'
            for idx in new_rights:
                ans[idx] = 'R'
            
            lefts = new_lefts
            rights = new_rights
        
        return ''.join(ans)