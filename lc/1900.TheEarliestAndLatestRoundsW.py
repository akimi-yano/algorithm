# 1900. The Earliest and Latest Rounds Where Players Compete
# Hard

# 65

# 9

# Add to List

# Share
# There is a tournament where n players are participating. The players are standing in a single row and are numbered from 1 to n based on their initial standing position (player 1 is the first player in the row, player 2 is the second player in the row, etc.).

# The tournament consists of multiple rounds (starting from round number 1). In each round, the ith player from the front of the row competes against the ith player from the end of the row, and the winner advances to the next round. When the number of players is odd for the current round, the player in the middle automatically advances to the next round.

# For example, if the row consists of players 1, 2, 4, 6, 7
# Player 1 competes against player 7.
# Player 2 competes against player 6.
# Player 4 automatically advances to the next round.
# After each round is over, the winners are lined back up in the row based on the original ordering assigned to them initially (ascending order).

# The players numbered firstPlayer and secondPlayer are the best in the tournament. They can win against any other player before they compete against each other. If any two other players compete against each other, either of them might win, and thus you may choose the outcome of this round.

# Given the integers n, firstPlayer, and secondPlayer, return an integer array containing two values, the earliest possible round number and the latest possible round number in which these two players will compete against each other, respectively.

 

# Example 1:

# Input: n = 11, firstPlayer = 2, secondPlayer = 4
# Output: [3,4]
# Explanation:
# One possible scenario which leads to the earliest round number:
# First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# Second round: 2, 3, 4, 5, 6, 11
# Third round: 2, 3, 4
# One possible scenario which leads to the latest round number:
# First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# Second round: 1, 2, 3, 4, 5, 6
# Third round: 1, 2, 4
# Fourth round: 2, 4
# Example 2:

# Input: n = 5, firstPlayer = 1, secondPlayer = 5
# Output: [1,1]
# Explanation: The players numbered 1 and 5 compete in the first round.
# There is no way to make them compete in any other round.
 

# Constraints:

# 2 <= n <= 28
# 1 <= firstPlayer < secondPlayer <= n

# This solution works:

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @lru_cache(None)
        def helper(mask, battles_left, get_min):
            if not battles_left:
                new_mask = list(mask)
                for i, elem in enumerate(new_mask):
                    if elem == 2:
                        new_mask[i] = 1
                # if we have no more battles left, start a new round
                return 1 + helper(tuple(new_mask), sum(new_mask) // 2, get_min)
            
            left_player = right_player = -1
            for player in range(n):
                is_playing = mask[player]
                if is_playing == 1:
                    left_player = player
                    break
            for player in range(n-1, -1, -1):
                is_playing = mask[player]
                if is_playing == 1:
                    right_player = player
                    break
            if left_player in strongest_players and right_player in strongest_players:
                return 0
            if left_player in strongest_players:
                # right_player loses
                new_mask = list(mask)
                new_mask[right_player] = 0
                new_mask[left_player] = 2
                return helper(tuple(new_mask), battles_left - 1, get_min)
            if right_player in strongest_players:
                # left_player loses
                new_mask = list(mask)
                new_mask[left_player] = 0
                new_mask[right_player] = 2
                return helper(tuple(new_mask), battles_left - 1, get_min)
            
            new_mask1 = list(mask)
            new_mask1[left_player] = 0
            new_mask1[right_player] = 2
            option1 = helper(tuple(new_mask1), battles_left - 1, get_min)
            
            new_mask2 = list(mask)
            new_mask2[right_player] = 0
            new_mask2[left_player] = 2
            option2 = helper(tuple(new_mask2), battles_left - 1, get_min)
            return min(option1, option2) if get_min else max(option1, option2)
            
        firstPlayer -= 1
        secondPlayer -= 1
        strongest_players = [firstPlayer, secondPlayer]
        
        mask = tuple([1] * n)
        
        return [helper(mask, 0, True), helper(mask, 0, False)]