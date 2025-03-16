'''
2594. Minimum Time to Repair Cars
Medium
Topics
Companies
Hint
You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.

You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

Return the minimum time taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.

 

Example 1:

Input: ranks = [4,2,3,1], cars = 10
Output: 16
Explanation: 
- The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
- The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
- The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
- The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​
Example 2:

Input: ranks = [5,1,8], cars = 6
Output: 16
Explanation: 
- The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
- The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
- The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​
 

Constraints:

1 <= ranks.length <= 105
1 <= ranks[i] <= 100
1 <= cars <= 106
'''

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def can_fix_with_this_time(time_limit):
            # since the mechanics can fix the cars in parallel, just calculate how many cars each can fix
            # which is n, and then check if the n is larger than or equal to cars to be fixed
            # formula is: If a mechanic with rank r can repair n cars in time t, then: r * n² ≤ t, so n = sqrt(t/r)
            fixed_cars = 0
            for rank in ranks:
                n = int(math.sqrt(time_limit/rank)) # t=r*n**2 -> n=sqrt(t/r)
                fixed_cars += n
                if fixed_cars >= cars:
                    return True
            return False

        left = 1 
        right = min(ranks) * cars * cars # The time it would take if the fastest mechanic repairs all cars alone

        while left < right:
            mid = (left + right) // 2
            if can_fix_with_this_time(mid):
                right = mid
            else:
                left = mid + 1
        return left
