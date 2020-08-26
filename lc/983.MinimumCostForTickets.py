# 983. Minimum Cost For Tickets

# In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

# Train tickets are sold in 3 different ways:

# a 1-day pass is sold for costs[0] dollars;
# a 7-day pass is sold for costs[1] dollars;
# a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

# Return the minimum number of dollars you need to travel every day in the given list of days.


# Example 1:

# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation: 
# For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total you spent $11 and covered all the days of your travel.
# Example 2:

# Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
# Output: 17
# Explanation: 
# For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
# On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
# In total you spent $17 and covered all the days of your travel.

# Note:

# 1 <= days.length <= 365
# 1 <= days[i] <= 365
# days is in strictly increasing order.
# costs.length == 3
# 1 <= costs[i] <= 1000



# Yay this solution works !!!!

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.p1 = costs[0]
        self.p7 = costs[1]
        self.p30 = costs[2]
        memo = {}
        def helper(i):
            if i in memo:
                return memo[i]
            
            if i > len(days)-1:
                return 0
            min_cost = float('inf')
        
            # Use 1 day pass
            min_cost = min(min_cost, (self.p1 + helper(i+1)))
            
            # Use 7 day pass
            start_day = days[i]
            usedP7 = False
            for k in range(i+1,len(days)):
                if days[k]-start_day >= 7:
                    usedP7 = True
                    min_cost = min(min_cost, (self.p7 + helper(k)))
                    break
            if not usedP7:
                min_cost = min(min_cost, self.p7)
            
            # Use 30 day pass
            start_day = days[i]
            usedP30 = False
            for j in range(i+1,len(days)):
                if days[j]-start_day >= 30:
                    usedP30 = True
                    min_cost = min(min_cost, (self.p30 + helper(j)))
                    break
            if not usedP30:
                min_cost = min(min_cost, self.p30)
            
            memo[i] = min_cost
            return min_cost
        
        return helper(0)