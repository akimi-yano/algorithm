# 1626. Best Team With No Conflicts
# Medium

# 83

# 4

# Add to List

# Share
# You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

# However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

# Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.

 

# Example 1:

# Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
# Output: 34
# Explanation: You can choose all the players.
# Example 2:

# Input: scores = [4,5,6,5], ages = [2,1,2,1]
# Output: 16
# Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.
# Example 3:

# Input: scores = [1,2,3,5], ages = [8,9,10,1]
# Output: 6
# Explanation: It is best to choose the first 3 players. 
 

# Constraints:

# 1 <= scores.length, ages.length <= 1000
# scores.length == ages.length
# 1 <= scores[i] <= 106
# 1 <= ages[i] <= 1000


# This approach does not work !

# class Solution:
#     def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
#         arr = []
#         for i in range((len(scores))):
#             arr.append((scores[i], ages[i]))
#         arr.sort(reverse=True)
        
        
#         def helper(i, prevscore, prevage):
#             if i > len(arr)-1:
#                 return 0
#             if arr[i][0] < prevscore and arr[i][1] > prevage:
#                 return 0
#             max_score = 0
#             max_score = max(max_score, arr[i][0] + helper(i+1,arr[i][0],arr[i][1]), helper(i+1,prevscore,prevage))
#             return max_score
        
#         return helper(0, float('-inf'), float('inf'))


# This solution does not work ! - TLE

# class Solution:
#     def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
#         arr = []
#         for i in range((len(scores))):
#             arr.append((scores[i], ages[i]))
#         arr.sort(reverse=True)
        
        
#         def helper(i, prevscore, prevage):
#             if i > len(arr)-1:
#                 return 0
#             if arr[i][0] < prevscore and arr[i][1] > prevage:
#                 return helper(i+1, prevscore, prevage)
#             max_score = 0
#             max_score = max(max_score, arr[i][0] + helper(i+1,arr[i][0],min(prevage, arr[i][1])), helper(i+1,prevscore,prevage))
#             return max_score
        
#         return helper(0, float('-inf'), float('inf'))


# This solution works ! DP

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        self.arr = []
        for i in range((len(scores))):
            self.arr.append((scores[i], ages[i]))
        self.arr.sort(reverse=True)

        self.memo ={}
        return self.helper(0, float('inf'))

    def helper(self, idx, min_age):
        key = (idx, min_age)
        if key in self.memo:
            return self.memo[key]

        ans = 0
        if idx >= len(self.arr):
            pass
        else:
            score, age = self.arr[idx]
            ans = self.helper(idx+1, min_age)
            if age <= min_age:
                ans = max(ans, score + self.helper(idx+1, age))
        self.memo[key] = ans
        return ans