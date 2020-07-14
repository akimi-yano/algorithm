# 1344. Angle Between Hands of a Clock

# Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

 

# Example 1:



# Input: hour = 12, minutes = 30
# Output: 165
# Example 2:



# Input: hour = 3, minutes = 30
# Output: 75
# Example 3:



# Input: hour = 3, minutes = 15
# Output: 7.5
# Example 4:

# Input: hour = 4, minutes = 50
# Output: 155
# Example 5:

# Input: hour = 12, minutes = 0
# Output: 0
 

# Constraints:

# 1 <= hour <= 12
# 0 <= minutes <= 59
# Answers within 10^-5 of the actual value will be accepted as correct.


# To solve this problem we need to understand the speeds of Hands of a clock.

# Let us find the place, where hour hand is. 
# First, whe have 12 hours in total, for 360 degrees, that means 30 degrees per hour. 
# Also, for every 60 minutes, our hour hand rotated by 1 hour, that is 30 degrees, 
# so for every minute, it is rotated by 0.5 degrees. 
# 
# So, final place for hour hand is 30*hour + 0.5*minutes
# Let us find the place, where minute hand is: every 60 minutes minute hand makes full rotation, 
# that means we have 6 degrees for each minute.

# Finally, we evaluate absolute difference between these two numbers, and if angle is more than 180 degrees, 
# we return complementary angle.
# Complexity: time and space is O(1), we just use some mathematical formula.

class Solution:
    def angleClock(self, hour, minutes):
        H_place = 30*hour + 0.5*minutes
        M_place = 6*minutes
        diff = abs(H_place - M_place)
        return diff if diff <= 180 else 360 - diff
    
    
# Oneliner
# We can write this as oneliner as well:

return min(abs(30*hour-5.5*minutes),360-abs(30*hour-5.5*minutes))



# Wrote detailed comments below

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        # HOUR HAND: 
        # First, whe have 12 hours in total, 
        # for 360 degrees, that means 30 degrees per hour (360/12=30) per hour
        # Also, for every 60 minutes, our hour hand rotated by 1 hour, 
        # that is 30 degrees, so for every minute, (30/60=0.5) per min
        # it is rotated by 0.5 degrees 
        # every hour, it moves 30 degrees
        # every minute, it moves 0.5 degrees
        H_place = 30*hour + 0.5*minutes
        
        # MINUTE HAND:
        # every 60 minutes minute hand makes full rotation, (360/60=60) per min
        # that means we have 6 degrees for each minute.
        # every minute, it moves 6 degrees
        M_place = 6*minutes
        
        # get difference between each degree
        diff = abs(H_place - M_place)
        # if the difference is smaller than 180 degrees then just return the diff
        # if the difference is larger than 180 degrees then subtract it from 360 because the other side is smaller in degree
        return diff if diff <= 180 else 360 - diff
        


# for this problem, you need to break down the problem to get each degree - :)
