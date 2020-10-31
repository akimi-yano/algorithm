# 849. Maximize Distance to Closest Person
# Medium

# 1063

# 125

# Add to List

# Share
# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

# There is at least one empty seat, and at least one person sitting.

# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

# Return that maximum distance to the closest person.


# Example 1:


# Input: seats = [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# Example 2:

# Input: seats = [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# Example 3:

# Input: seats = [0,1]
# Output: 1

# Constraints:

# 2 <= seats.length <= 2 * 104
# seats[i] is 0 or 1.
# At least one seat is empty.
# At least one seat is occupied.



# This approach does not work 

# class Solution:
#     def maxDistToClosest(self, seats: List[int]) -> int:
#         if sum(seats) == 1:
#             return len(seats)-1
#         max_distance = 0
#         count = 1
#         for i in range(len(seats)):
#             if seats[i]:
#                 max_distance = max(max_distance, count)
#                 count = 1
#             else:
#                 count += 1
#         max_distance = max(max_distance, count)
#         return max_distance//2


# This approach does not work 

# class Solution:
#     def maxDistToClosest(self, seats: List[int]) -> int:
#         # [1,0,0,0,1,0,1]
#          #   s
#          #         e
#          # d = f
#          # max
#         start = end = 0
#         divide = True
#         max_dist = 0
#         while start < len(seats):
#             if seats[start]:
#                 start+=1 
#             else:
#                 end = start
#                 while end < len(seats) and not seats[end]:
#                     end +=1
                
#                 if (end-start) >= max_dist:
#                     max_dist = end-start
#                     if start == 0 or start ==len(seats)-1 or end == len(seats):
#                         divide &= False
#                     else:
#                         divide &= True
#                 start += 1
#         if divide:
#             return (max_dist+1)//2
#         else:
#             return max_dist


# This approach does not work 

# class Solution:
#     def maxDistToClosest(self, seats: List[int]) -> int:
#         # [1,0,0,0,1,0,1]
#          #   s
#          #         e
#          # d = f
#          # max
#         start = end = 0
#         divide = True
#         max_dist = 0
#         while start < len(seats):
#             if seats[start]:
#                 start+=1 
#             else:
#                 end = start
#                 while end < len(seats) and not seats[end]:
#                     end +=1
                
#                 if (end-start) >= max_dist:
#                     max_dist = end-start
#                     if start == 0 or start ==len(seats)-1 or end == len(seats):
#                         divide &= False
#                     else:
#                         divide &= True
#                 start += 1
#         if divide:
#             return (max_dist+1)//2
#         else:
#             return max_dist


# This solution works !

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_num_0 = 0
        count = 0
        for elem in seats:
            if not elem:
                count+=1
                max_num_0 = max(max_num_0, (count+1)//2)
            else:
                count = 0
        count = 0
        for elem in seats:
            if elem:
                break
            count += 1
        max_num_0 = max(max_num_0, count)
        count = 0
        for elem in reversed(seats):
            if elem:
                break
            count += 1
        max_num_0 = max(max_num_0, count)
    
        return max_num_0
    
    
# This solution works ! Optimization ! - cleaner code

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_num_0 = 0
        prev = -1
        for i, elem in enumerate(seats):
            if elem:
                if prev < 0:
                    # if prev < 0, this is the begining. No need to divide by 2.
                    max_num_0 = max(max_num_0, i-prev-1)
                else:
                    # else, we are in the middle. Divide by 2.
                    max_num_0 = max(max_num_0, (i-prev)//2)
                prev = i
        # No need to divide by 2 at the end.
        max_num_0 = max(max_num_0, len(seats) - prev - 1)
    
        return max_num_0