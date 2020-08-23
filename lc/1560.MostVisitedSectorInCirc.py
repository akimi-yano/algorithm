# 1560. Most Visited Sector in a Circular Track

# Given an integer n and an integer array rounds. We have a circular track which consists of n sectors labeled from 1 to n. A marathon will be held on this track, the marathon consists of m rounds. The ith round starts at sector rounds[i - 1] and ends at sector rounds[i]. For example, round 1 starts at sector rounds[0] and ends at sector rounds[1]

# Return an array of the most visited sectors sorted in ascending order.

# Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise direction (See the first example).



# Example 1:


# Input: n = 4, rounds = [1,3,1,2]
# Output: [1,2]
# Explanation: The marathon starts at sector 1. The order of the visited sectors is as follows:
# 1 --> 2 --> 3 (end of round 1) --> 4 --> 1 (end of round 2) --> 2 (end of round 3 and the marathon)
# We can see that both sectors 1 and 2 are visited twice and they are the most visited sectors. Sectors 3 and 4 are visited only once.
# Example 2:

# Input: n = 2, rounds = [2,1,2,1,2,1,2,1,2]
# Output: [2]
# Example 3:

# Input: n = 7, rounds = [1,3,5,7]
# Output: [1,2,3,4,5,6,7]


# Constraints:

# 2 <= n <= 100
# 1 <= m <= 100
# rounds.length == m + 1
# 1 <= rounds[i] <= n
# rounds[i] != rounds[i + 1] for 0 <= i < m





# These solutions don't work ....

# v1
# class Solution:
#     def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
#         arr = [0 for _ in range(n)]

#         for i in range(len(rounds)-1):
#             if rounds[i]>rounds[i+1]:
#                 end = n+1
#             else:
#                 end = rounds[i+1]
#             for k in range(rounds[i],end):
#                 arr[k-1]+=1

#         arr[rounds[-1]-1]+=1
            
#         max_val = max(arr)
#         ans = []
#         for j in range(len(arr)):
#             if arr[j] == max_val:
#                 ans.append(j+1)
#         return ans

# v2
# class Solution:
#     def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
#         arr = [0 for _ in range(n)]
#         arr[rounds[0]-1]+=1
#         for i in range(1,len(rounds)):
#             for k in range(rounds[i-1],rounds[i]+1):
#                 arr[(k)%(n+1)-1]+=1
#                 print(k)
#             # print('*'*10)

#         # arr[rounds[-1]-1]+=1
#         print(arr)
#         max_val = max(arr)
#         ans = []
#         for j in range(len(arr)):
#             if arr[j] == max_val:
#                 ans.append(j+1)
#         return ans


# This solution works !!!

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        arr = [0 for _ in range(n)]
        arr[rounds[0]-1]+=1
        for i in range(1,len(rounds)):
            # if the current sector is >= previous sector
            if rounds[i-1] <= rounds[i]:
                for k in range(rounds[i-1]+1,rounds[i]+1):
                    arr[k-1]+=1
            # else, sector loops around
            else:
                # go to the last sector
                for k in range(rounds[i-1]+1,n+1):
                    arr[k-1]+=1
                # start from the first sector
                for k in range(1,rounds[i]+1):
                    arr[k-1]+=1
        max_val = max(arr)
        ans = []
        for j in range(len(arr)):
            if arr[j] == max_val:
                ans.append(j+1)
        return ans

