'''
486. Predict the Winner
Medium
5.6K
258
Companies
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.

 

Example 1:

Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return false.
Example 2:

Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 107
'''

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        '''
        ones: try to maximize
        twos: try to minimize ones next iteration of total
        just keep track of ones total and subtract from the sum of nums at the end
        to calculate ones future ones, it would be after twos choosing elements to make the next total of ones to be minimim
        '''
        def helper(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left == right:
                return nums[left]
            elif left > right:
                return 0
            
            # if player 1 chooses left, the player 2 chooses left+1 or right -> so player 1 will have left+2 and right or left+1 and right -1 -> so get their minimim
            option1 = nums[left] + min(helper(left+2, right),helper(left+1, right-1))
            # if player 1 chooses right, the player 2 chooses left or right -1 -> so player 1 will have left+1 and right -1 or left and right -2
            option2 = nums[right] + min(helper(left+1, right-1), helper(left, right-2))
            bestForOne = max(option1, option2)
            memo[(left, right)] = bestForOne
            return bestForOne
        
        memo = {}
        ones = helper(0, len(nums)-1)
        total = sum(nums)
        twos = total - ones
        return ones >= twos