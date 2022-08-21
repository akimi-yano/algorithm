# <!-- 871. Minimum Number of Refueling Stops
# Hard

# 3853

# 75

# Add to List

# Share
# A car travels from a starting position to a destination which is target miles east of the starting position.

# There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

# The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

# Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

# Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

 

# Example 1:

# Input: target = 1, startFuel = 1, stations = []
# Output: 0
# Explanation: We can reach the target without refueling.
# Example 2:

# Input: target = 100, startFuel = 1, stations = [[10,100]]
# Output: -1
# Explanation: We can not reach the target (or even the first gas station).
# Example 3:

# Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
# Output: 2
# Explanation: We start with 10 liters of fuel.
# We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
# Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
# and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
# We made 2 refueling stops along the way, so we return 2.
 

# Constraints:

# 1 <= target, startFuel <= 109
# 0 <= stations.length <= 500
# 0 <= positioni <= positioni+1 < target
# 1 <= fueli < 109 -->


# This solution works: 

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0

        cur_stops = {}
        cur_stops[0] = startFuel

        ans = set([])
        for next_distance, refuel in stations:
            new_cur_stops = {}
            for stops, max_distance in cur_stops.items():
                if max_distance < next_distance:
                    continue
                new_cur_stops[stops + 1] = max_distance + refuel
            
            for stops, max_distance in cur_stops.items():
                if stops not in new_cur_stops or new_cur_stops[stops] < max_distance:
                    new_cur_stops[stops] = max_distance
            
            for stops, max_distance in new_cur_stops.items():
                if max_distance >= target:
                    ans.add(stops)

            cur_stops = new_cur_stops
        
        
        if not ans:
            return -1
        return min(ans)