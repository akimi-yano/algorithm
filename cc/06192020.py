# It consists of 2 questions that we ask that you complete in Python. 
# There is a 76 minute time limit, but expect that many people can finish in significantly less time. 

# Correctness is important, but equally important is the clarity and elegance of your code. 
# We will be evaluating your solutions with both of these factors in mind.


# 1. Encircular
# Build a computer simulation of a mobile robot. The robot moves on an infinite plane, starting from position (0, 0). 
# Its movements are described by a command string consisting of one or more of the following three letters:

# G instructs the robot to move forward one step.
# L instructs the robot to turn left in place.
# R instructs the robot to turn right in place.

# The robot performs the instructions in a command sequence in an infinite loop. 
# Determine whether there exists some circle such that the robot always moves within the circle.

# Consider the commands R and G executed infinitely.  A diagram of the robot's movement looks like:

# RG → RG
# ↑     ↓
# RG ← RG

# The robot will never leave the circle.

# Function Description 

# Complete the function doesCircleExist in the editor below. The function must return an array of n strings either YES or NO 
# based on whether the robot is bound within a circle or not, in order of test results.

# doesCircleExist has the following parameter(s):
#     commands[commands[0],...commands[n-1]]:  An array of n commands[i] where each represents a list of commands to test.

# Constraints

# 1 ≤ |commands[i]| ≤ 2500
# 1 ≤ n ≤ 10
# Each command consists of G, L, and R only.

# Input Format for Custom Testing
# Sample Case 0
# Sample Input 0

# 2
# G
# L

# Sample Output 0

# NO
# YES

# Explanation 0

# There are n = 2 commands:

# For commands[0] = "G", the robot will move forward forever ( G → G → G →... ) without ever turning or being restricted to a circle. 
# Set index 0 of the return array to NO.
# For commands[1] = "L", the robot will just turn 90 degrees left forever without ever moving forward (because there is no "G" 
# instruction). The robot is effectively trapped at one spot, thus bound within a circle. Set index 1 of the return array to YES .


# #
# # Complete the 'doesCircleExist' function below.
# #
# # The function is expected to return a STRING_ARRAY.
# # The function accepts STRING_ARRAY commands as parameter.
# #


# Complete the 'doesCircleExist' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY commands as parameter.


# def doesCircleExist(commands):
#     moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#     ans = []
#     for command in commands:
#         move_idx = 0
#         cur = [0, 0]
#         # repeating the commands 4 times is sufficient to come back to the original position
#         for _ in range(4):
#             for c in command:
#                 if c == 'R':
#                     move_idx = (move_idx+1) % 4
#                 elif c == 'L':
#                     move_idx = (move_idx-1) % 4
#                 elif c == 'G':
#                     cur = [sum(dim) for dim in zip(cur, moves[move_idx])]
#         if cur == [0, 0]:
#             ans.append('YES')
#         else:
#             ans.append('NO')
#     return ans

def doesCircleExist(commands):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ans = []
    for command in commands:
        move_idx = 0
        cur = [0, 0]
        # repeating the commands 4 times is sufficient to come back to the original position
        for _ in range(4):
            for c in command:
                if c == 'R':
                    move_idx = (move_idx+1) % 4
                elif c == 'L':
                    move_idx = (move_idx-1) % 4
                elif c == 'G':
                    # cur = [sum(dim) for dim in zip(cur, moves[move_idx])]
                    move_x, move_y = moves[move_idx]
                    cur[0], cur[1] = cur[0]+move_x, cur[1]+move_y
        if cur == [0, 0]:
            ans.append('YES')
        else:
            ans.append('NO')
    return ans



# 2. Throttling Gateway
# Non-critical requests for a transaction system are routed through a throttling gateway to ensure that the network is not choked 
# by non-essential requests.

# The gateway has the following limits:

# The number of transactions in any given second cannot exceed 3.
# The number of transactions in any given 10 second period cannot exceed 20. A ten-second period includes all requests arriving 
# from any time max(1, T-9) to T (inclusive of both) for any valid time T.
# The number of transactions in any given minute cannot exceed 60.   Similar to above, 1 minute is from max(1, T-59) to T.

# Any request that exceeds any of the above limits will be dropped by the gateway. Given the times at which different requests 
# arrive sorted ascending, find how many requests will be dropped.

# Note: Even if a request is dropped it is still considered for future calculations. Although, if a request is to be dropped due 
# to multiple violations, it is still counted only once.


# Example

# n = 27

# requestTime = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11 ] 

# Request 1 - Not Dropped.
# Request 1 - Not Dropped.
# Request 1 - Not Dropped.
# Request 1 - Dropped. At most 3 requests are allowed in one second.
# No request will be dropped till 6 as all comes at an allowed rate of 3 requests per second and the 10-second clause is also not 
# violated.
# Request 7 - Not Dropped. The total number of requests has reached 20 now.
# Request 7 - Dropped. At most 20 requests are allowed in ten seconds.
# Request 7 - Dropped. At most 20 requests are allowed in ten seconds.
# Request 7 - Dropped. At most 20 requests are allowed in ten seconds. Note that the 1-second limit is also violated here.
# Request 11 - Not Dropped. The 10-second window has now become 2 to 11. Hence the total number of requests in this window is 20 now.
# Request 11 - Dropped. At most 20 requests are allowed in ten seconds.
# Request 11 - Dropped. At most 20 requests are allowed in ten seconds.
# Request 11 - Dropped. At most 20 requests are allowed in ten seconds. Also, at most 3 requests are allowed per second.
# Hence, a total of 7 requests are dropped.


# Function Description

# Complete the droppedRequests function in the editor below.


# droppedRequests has the following parameter(s):

#     int requestTime[n]: an ordered array of integers that represent the times of various requests

# Returns

#     int:  the total number of dropped requests


# Constraints

# 1 ≤ n ≤ 106
# 1 ≤ requestTime[i] ≤ 109

# Input Format For Custom Testing
# Sample Case 0
# Sample Input For Custom Testing

# STDIN     Function 
# -----     --------
# 5    →    requestTime[] size n = 5
# 1    →    requestTime = [ 1, 1, 1, 1, 2 ] 
# 1
# 1
# 1
# 2
# Sample Output

# 1
# Explanation

# There are 4 requests that arrive at second 1. This exceeds the per second limit so one packet is dropped. 
# No other limits are exceeded.



# Complete the 'droppedRequests' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY requestTime as parameter.
#

# this doenst work !
# def droppedRequests(requestTime):
#     checker = [1]*len(requestTime)
#     temp = requestTime[0]
#     counter = 0 
#     # check for the first condition
#     for i in range(len(requestTime)):
#         if requestTime[i]==temp:
#             counter+=1
#             if counter >3:
#                 checker[i]=0
#                 counter-=1
#         else:
#             temp = requestTime
#             counter = 0
#     # check for the second condition
#     #look for 10 using binary search
#     max_num = requestTime[len(requestTime)-1]
#     for i in range(10,max_num+10,10):

#     low = 0
#     high = len(requestTime)-1
#     while low<high:
#         mid = (low +high)//2
#         if requestTime[mid]==i and requestTime[mid+1]!=1:
            

#         elif requestTime[mid]<i:
#             pass
#     # check for the third condition



#     # count the # of drops
#     total =0
#     for c in checker:
#         if c==0:
#             total+=1
#     return total
    
    
    


from collections import deque
#
# Complete the 'droppedRequests' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY requestTime as parameter.
#

def droppedRequests(requestTime):
    three = deque([])
    twenty = deque([])
    sixty = deque([])
    num_dropped = 0
    for request in requestTime:
        if len(three) >= 3 and request-three[0] < 1:
            # print("dropping three: "+str(request))
            num_dropped += 1
        elif len(twenty) >= 20 and request-twenty[0] < 10:
            # print("dropping twenty: "+str(request))
            num_dropped += 1
        elif len(sixty) >= 60 and request-sixty[0] < 60:
            # print("dropping sixty: "+str(request))
            num_dropped += 1
        three.append(request)
        twenty.append(request)
        sixty.append(request)
        if len(three) > 3:
            three.popleft()
        if len(twenty) > 20:
            twenty.popleft()
        if len(sixty) > 60:
            sixty.popleft()
    return num_dropped






