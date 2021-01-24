# 1733. Minimum Number of People to Teach
# Medium

# 38

# 155

# Add to List

# Share
# On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

# You are given an integer n, an array languages, and an array friendships where:

# There are n languages numbered 1 through n,
# languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
# friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
# You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

# Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.
 

# Example 1:

# Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
# Output: 1
# Explanation: You can either teach user 1 the second language or user 2 the first language.
# Example 2:

# Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
# Output: 2
# Explanation: Teach the third language to users 1 and 3, yielding two users to teach.
 

# Constraints:

# 2 <= n <= 500
# languages.length == m
# 1 <= m <= 500
# 1 <= languages[i].length <= n
# 1 <= languages[i][j] <= n
# 1 <= u​​​​​​i < v​​​​​​i <= languages.length
# 1 <= friendships.length <= 500
# All tuples (u​​​​​i, v​​​​​​i) are unique
# languages[i] contains only unique values

# This solution works:
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # 1 make a dictionary of person-set of languages that the person can speak
        # 2 eliminate pairs who can already communicate with current languages, by using intersection() for the sets and 
        # only add to a list if there is no common languages
        # 3 iterate through each language and brute force (its ok as the constraints is only 500 each) and iterate through the pairs, for every language, initialize a set to keep track of the count of number of people to teach, and keep track of the min
        # and return the min
        person_langs = {}
        for i, lang in enumerate(languages):
            person_langs[i+1] = set(lang)
        
        pairs_to_teach = []
        for a, b in friendships:
            if not person_langs[a].intersection(person_langs[b]):
                pairs_to_teach.append((a, b))
        
        best = float('inf')
        for lang in range(1, n+1):
            taught_ppl = set([])
            for a, b in pairs_to_teach:
                if lang not in person_langs[a]:
                    taught_ppl.add(a)
                if lang not in person_langs[b]:
                    taught_ppl.add(b)
            best = min(best, len(taught_ppl))
        return best
    



# This approach does not work

# class Solution:
#     def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
#         def helper(i):
#             if i > len(friendships)-1:
#                 return 0
#             node1, node2 = friendships[i]
#             min_steps = float('inf')
#             for option in langs[node1-1]:
#                 if option in langs[node2-1]:
#                     min_steps = 0
#                     break
#             else:
#                 for option in langs[node1-1]:
#                     langs[node2-1].add(option)
#                     min_steps = min(min_steps, 1 + helper(i+1))
#                     langs[node2-1].remove(option)
            
#             for option in langs[node2-1]:
#                 if option in langs[node1-1]:
#                     min_steps = 0
#                     break
#             else:
#                 for option in langs[node2-1]:
#                     langs[node1-1].add(option)
#                     min_steps = min(min_steps, 1 + helper(i+1))
#                     langs[node1-1].remove(option)
#             return min_steps
        
#         langs = []
#         for lang in languages:
#             langs.append(set(lang))
#         return helper(0)