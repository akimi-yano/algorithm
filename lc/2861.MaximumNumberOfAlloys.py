'''
2861. Maximum Number of Alloys
Medium
44
16
Companies
You are the owner of a company that creates alloys using various types of metals. There are n different types of metals available, and you have access to k machines that can be used to create alloys. Each machine requires a specific amount of each metal type to create an alloy.

For the ith machine to create an alloy, it needs composition[i][j] units of metal of type j. Initially, you have stock[i] units of metal type i, and purchasing one unit of metal type i costs cost[i] coins.

Given integers n, k, budget, a 1-indexed 2D array composition, and 1-indexed arrays stock and cost, your goal is to maximize the number of alloys the company can create while staying within the budget of budget coins.

All alloys must be created with the same machine.

Return the maximum number of alloys that the company can create.

 

Example 1:

Input: n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,0], cost = [1,2,3]
Output: 2
Explanation: It is optimal to use the 1st machine to create alloys.
To create 2 alloys we need to buy the:
- 2 units of metal of the 1st type.
- 2 units of metal of the 2nd type.
- 2 units of metal of the 3rd type.
In total, we need 2 * 1 + 2 * 2 + 2 * 3 = 12 coins, which is smaller than or equal to budget = 15.
Notice that we have 0 units of metal of each type and we have to buy all the required units of metal.
It can be proven that we can create at most 2 alloys.
Example 2:

Input: n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,100], cost = [1,2,3]
Output: 5
Explanation: It is optimal to use the 2nd machine to create alloys.
To create 5 alloys we need to buy:
- 5 units of metal of the 1st type.
- 5 units of metal of the 2nd type.
- 0 units of metal of the 3rd type.
In total, we need 5 * 1 + 5 * 2 + 0 * 3 = 15 coins, which is smaller than or equal to budget = 15.
It can be proven that we can create at most 5 alloys.
Example 3:

Input: n = 2, k = 3, budget = 10, composition = [[2,1],[1,2],[1,1]], stock = [1,1], cost = [5,5]
Output: 2
Explanation: It is optimal to use the 3rd machine to create alloys.
To create 2 alloys we need to buy the:
- 1 unit of metal of the 1st type.
- 1 unit of metal of the 2nd type.
In total, we need 1 * 5 + 1 * 5 = 10 coins, which is smaller than or equal to budget = 10.
It can be proven that we can create at most 2 alloys.
 

Constraints:

1 <= n, k <= 100
0 <= budget <= 108
composition.length == k
composition[i].length == n
1 <= composition[i][j] <= 100
stock.length == cost.length == n
0 <= stock[i] <= 108
1 <= cost[i] <= 100
'''

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        '''
        Intuition
        The question is a more complex looking type of binary search problems called "Binary Search over Solution Space". This is a premium only category in LeetCode's own binary search plan.

        This question is a variant of the classic 875. Koko Eating Bananas problem and has been modified to just look complex.

        Approach
        Since we can only use any one machine to make alloys, we can calculate the maximum alloys each machine can make and then return the answer accordingly.

        First, we assume that we can make anywhere from left = 0 to right = 10**10 alloys from a single machine (arbitrarily high value).

        Then, we check if we can make exactly mid = (left + right) // 2 alloys from it.

        If we can, it means we may still be able to make more, so we shift left = mid + 1 and shift the search space upwards. If we can't make those many alloys, we do right = mid and shift the search space downwards. We do this till left < right.

        At the end, left will be the upper bound of our range, i.e. it will the first value that we won't be able to make from our machines. Hence, left - 1 will be our answer here.

        We repeat this process over all the machines and return the maximum value we could make.

        Explanation of can_make(machine, num_alloys):
        We pass a machine to the function which we'll calculate with respect to.

        We know to build the alloy, we'll need composition[machine][metal_idx] of the i'th metal. Hence the total i'th metal needed to build num_alloys number of alloys is composition[machine][metal_idx] * num_alloys.

        Now since we may already have some of it in stock, we just need an additional composition[machine][metal_idx] * num_alloys - stock[metal_idx] amount of this metal. The price for it would be (composition[machine][metal_idx] * num_alloys - stock[metal_idx]) * cost[metal_idx].

        But it is also possible that we may have more than the required metal in stock, in which case we don't need to buy any more metal. For that, we can do (max(0, composition[machine][metal_idx] * num_alloys - stock[metal_idx]) * cost[metal_idx]) to cut the price off at 0 if it falls below it due to negative subtraction.

        Finally, if the current price <= budget, we return True, else we return False. A simpler way of writing would be to say return price <= budget, as price <= budget inherently evaluates as true or false itself.

        Complexity
        Time complexity:
        O(log(10^10) * k * n) for search space * k machines * n metals while calculating price.
        Space complexity:
        O(1)
        Code

        '''
        """
        n = Types of metals available
        k = number of machines available

                        metals
        composition = [[1, 2, 3],   machine 1
                       [4, 5, 6]]   machine 2

        (Metals needed by machine to build alloy)

        stock = [] number of i'th metal already available
        cost = [] cost to buy more of the i'th metal

        budget = maximum limit to not exceed

        """
        ans = 0

        def can_make(machine, num_alloys):
            # See if we can make num_alloys
            price = 0
            for metal in range(n):
                price += (max(0, composition[machine][metal] * num_alloys - stock[metal]) * cost[metal])

            return price <= budget

        for machine in range(k):
            # At any point we can have only at most say 10**10 alloys
            left, right = 0, 10**10

            while left < right:
                mid = left + (right - left) // 2

                if can_make(machine, mid):
                    left = mid + 1
                else:
                    right = mid

            ans = max(ans, left)

        return ans - 1