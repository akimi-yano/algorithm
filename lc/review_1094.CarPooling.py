# 1094. Car Pooling
# Medium

# 1800

# 47

# Add to List

# Share
# There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

# You are given the integer capacity and an array trips where trip[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

# Example 1:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false
# Example 2:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true
 

# Constraints:

# 1 <= trips.length <= 1000
# trips[i].length == 3
# 1 <= numPassengersi <= 100
# 0 <= fromi < toi <= 1000
# 1 <= capacity <= 105


# This solution works:


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # use the locations points as there are only 1000 possibilities
        locs = [0 for _ in range(0, 1001)]
        
        # keep track of the delta
        for num_ppl, from_loc, to_loc in trips:
            locs[from_loc] += num_ppl
            locs[to_loc] -= num_ppl
        
        # use delta to keep track of the actual number of ppl
        cur = 0
        for i, delta in enumerate(locs):
            cur += delta
            locs[i] = cur
        
        # check if the number of ppl exceeds the capacity at any point
        for ppl in locs:
            if ppl > capacity:
                return False
        return True