# 134. Gas Station
# Medium

# 2164

# 396

# Add to List

# Share
# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

# Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

# Note:

# If there exists a solution, it is guaranteed to be unique.
# Both input arrays are non-empty and have the same length.
# Each element in the input arrays is a non-negative integer.
# Example 1:

# Input: 
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]

# Output: 3

# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.
# Example 2:

# Input: 
# gas  = [2,3,4]
# cost = [3,4,3]

# Output: -1

# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
# Therefore, you can't travel around the circuit once no matter where you start.



# This solution works but not the optimal !:
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for offset in range(len(gas)):
            # print(offset)
        # offset = 3
            prev = 0
            total = 0
            found = False
            seen = set([])
            for i in range(len(gas)):
                idx = (i+ offset) % len(gas)
                seen.add(idx)
                total += -prev + gas[idx]

                prev = cost[idx]
                if total - prev < 0:
                    break
                if len(seen) == len(gas):
                    found = True
                # print(total)
            if found:
                if (total - prev) >= 0:
                    return offset
                else:
                    found = False
        return -1
    
    

# This solution does not work :
            # print(idx)
#         '''
#         Input: 
#         gas  = [1,2,3,4,5]
#         cost = [3,4,5,1,2]

#         Output: 3

#         Explanation:
#         Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
#         Travel to station 4. Your tank = 4 - 1 + 5 = 8
#         Travel to station 0. Your tank = 8 - 2 + 1 = 7
#         Travel to station 1. Your tank = 7 - 3 + 2 = 6
#         Travel to station 2. Your tank = 6 - 4 + 3 = 5
#         Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
#         Therefore, return 3 as the starting index.

#         '''
#         def helper(i,prev, seen):
#             idx = i% len(gas)
#             if idx in seen:
#                 if len(seen) == len(gas):
#                     return 0
#                 # else:
#                 #     return float('-inf')
#             seen.add(idx)
#             total = 0 
#             total += gas[idx] - prev
#             # print(total)
#             # if total < 0:
#             #     return float('-inf')
#             total += helper(i-1, cost[idx], seen)
            
# #             if total < 0:
# #                 return float('-inf')
            
#             return total
        
#         # for start in range(len(gas)):
#         maybe_ans = helper(3,0, set([]))
#         # print(maybe_ans)
#             # if maybe_ans != float('-inf'):
#             #     return start
#         return -1
            
            
            
            
# This solution works !!!:

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_index = 0
        current_fuel = 0
        N = len(gas)
        # step1: find start index 
        for i in range(N):
            current_fuel += gas[i] - cost[i]
            # if you run out of fuel, reset and try from the next index.
            if current_fuel < 0:
                start_index = i + 1
                current_fuel = 0
        
        if start_index >= N:
            return -1
        
        # step2: verify the start index 
        cur = 0
        for i in range(N):
            idx = (i + start_index) % N
            cur += gas[idx] - cost[idx]
            if cur < 0:
                return -1
        return start_index