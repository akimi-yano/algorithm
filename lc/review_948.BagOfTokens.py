# 948. Bag of Tokens
# Medium

# 1140

# 347

# Add to List

# Share
# You have an initial power of power, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

# Your goal is to maximize your total score by potentially playing each token in one of two ways:

# If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
# If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
# Each token may be played at most once and in any order. You do not have to play all the tokens.

# Return the largest possible score you can achieve after playing any number of tokens.

 

# Example 1:

# Input: tokens = [100], power = 50
# Output: 0
# Explanation: Playing the only token in the bag is impossible because you either have too little power or too little score.
# Example 2:

# Input: tokens = [100,200], power = 150
# Output: 1
# Explanation: Play the 0th token (100) face up, your power becomes 50 and score becomes 1.
# There is no need to play the 1st token since you cannot play it face up to add to your score.
# Example 3:

# Input: tokens = [100,200,300,400], power = 200
# Output: 2
# Explanation: Play the tokens in this order to get a score of 2:
# 1. Play the 0th token (100) face up, your power becomes 100 and score becomes 1.
# 2. Play the 3rd token (400) face down, your power becomes 500 and score becomes 0.
# 3. Play the 1st token (200) face up, your power becomes 300 and score becomes 1.
# 4. Play the 2nd token (300) face up, your power becomes 0 and score becomes 2.
 

# Constraints:

# 0 <= tokens.length <= 1000
# 0 <= tokens[i], power < 104


# This solution works:


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        '''
        1 sort x
        2 turn the tokens arr into queue x
        3 pop from left to gain score and lose power : while we have enough P x
        4 pop from right to lose score but to gain points (only if we have enough score and we have 1 more or more elements to gain more scores)
        '''
        tokens.sort()
        score = 0
        left = 0
        right = len(tokens)-1
        
        while left <= right:
            # 1 option - lose power to gain score
            if P >= tokens[left]:
                P -= tokens[left]
                score += 1
                left += 1
            # 2 option - lose score to gain power
            elif left + 1 <= right and score >=1:
                P += tokens[right]
                score -=1 
                right -= 1
            # 3 option - don't do anything
            else:
                break
                
        return score
        
