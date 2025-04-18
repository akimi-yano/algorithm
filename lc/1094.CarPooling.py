# 1094. Car Pooling
# Medium

# 814

# 33

# Add to List

# Share
# You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

# Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

# Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

 

# Example 1:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false
# Example 2:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true
# Example 3:

# Input: trips = [[2,1,5],[3,5,7]], capacity = 3
# Output: true
# Example 4:

# Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
# Output: true
 
 

# Constraints:

# trips.length <= 1000
# trips[i].length == 3
# 1 <= trips[i][0] <= 100
# 0 <= trips[i][1] < trips[i][2] <= 1000
# 1 <= capacity <= 100000


# THIS SOLUTION WORKS !!!
'''
sweep line approache!
1 make an arr with val 0 up to 1001 which is the constraints
2 increment the val at the start idx by num_riders
3 decrement the val at the end idx by num_riders
4 keep track of the accumulative sum cur to see if it goes over the capacity limit anytime then return False
5 after the end of the loop return True

'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0 for _ in range(1001)]
        for num_riders, start, end in trips:
            arr[start] += num_riders
            arr[end] -= num_riders
        
        cur = 0
        for i in range(len(arr)):
            cur += arr[i]
            if cur > capacity:
                return False
        return True
            