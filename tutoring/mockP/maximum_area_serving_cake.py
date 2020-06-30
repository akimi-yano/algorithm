# Maximum Area Serving Cake

# Given an array containing the radii of circular cakes and the number of guests, 
# determine the largest piece that can be cut from the cakes such that every guest 
# gets a piece of the cake with the same area. It is not possible that a single 
# piece has some part of one cake and some part of another cake and each guest is 
# served only one piece of cake.

# Example 1:

# Input: radii = [1, 1, 1, 2, 2, 3],  numberOfGuests = 6.
# Output: 7.0686

# Explanation:
# Reason being you can take the area of the cake with a radius of 3, and divide by 4. 
# (Area  28.743 / 4  = 7.0686)
# Use a similary sized piece from the remaining cakes of radius 2 because total area 
# of cakes with radius 2 are > 7.0686

# Example 2:

# Input: radii = [4, 3, 3], numberOfGuests = 3
# Output: 28.2743

# Example 3:

# Input: radii = [6, 7], numberOfGuests = 12
# Output: 21.9911

# def max_area_serving_cake(radii,numberOfGuests):
#     pass

# print(max_area_serving_cake([1, 1, 1, 2, 2, 3],6))



import math


def getArea(radius):
    return math.pi*radius*radius


def getCakeMax(cakes, P):
    
    
    def dfs(P, index):
        if index == len(cakes):
            return float('inf') if P == 0 else float('-inf')
        ans = 0
        # We can choose to not cut this cake
        no_cut = dfs(P, index+1)
        
        # Or we can choose to cut it from up to 1 to P slices (P remaining people...)
        # We want the largest value in the path
        #That's bounded by the current value (because all slices have to be equal)
        
        cut_max = float('-inf')
        for i in range(1, P+1):
            area = getArea(cakes[index])/i
            bestSolution = dfs(P-i, index+1)
            cut_max = max(cut_max, min(area, bestSolution))
        return max(no_cut, cut_max)
    return dfs(P, 0)

print("Knapsack +memo solution",getCakeMax([1],1))
print("Knapsack +memo solution",getCakeMax([ 1, 1, 1, 2, 2, 3],6))
print("Knapsack +memo solution",getCakeMax([4, 3, 3],3))
print("Knapsack +memo solution",getCakeMax([6, 7],12))
        

def getMaxCakeDP(cakes, P):
    def getArea(cake):
        return math.pi * cake * cake
    N = len(cakes)
    dp = []
    for i in range(0, P + 1):
        dp.append([0]* (N + 1))

    for i in range(1, N + 1):
        dp[1][i] = getArea(cakes[i - 1])

    for p in range(2, P + 1):
        for i in range(1, N + 1):
            dp[p][i] = getArea(cakes[i - 1]) / p
            for j in range(1, P + 1):
                dp[p][i] = max(min(dp[p - j][i - 1], getArea(cakes[i - 1]) / j), dp[p][i])

    return dp[P][N]

print("DP solution",getMaxCakeDP([ 1, 1, 1, 2, 2, 3], 6))
print("DP solution",getMaxCakeDP([4, 3, 3], 3))
print("DP solution",getMaxCakeDP([6, 7], 12)) 


# https://leetcode.com/discuss/interview-question/348510/google-online-assessment-maximum-area-serving-cake

# Simple binary search python solution, complexity is O(log(A/epsilon) * n), 
# where n is number of cakes, A is the largest area, epsilon is the precision tolerance 

def maximumAreaServingCake(radii, numberOfGuests):
    areas = [math.pi * r * r for r in radii]
    def possible(x):
        k = 0
        for a in areas:
            k += a // x
            if k >= numberOfGuests:
                return True
        return False
    
    l, r = 0, max(areas)
    while l + 1e-5 <= r:
        x = (l + r) / 2
        if possible(x):
            l = x
        else:
            r = x
    return round(x, 4)

# Example 1.
radii = [ 1, 1, 1, 2, 2, 3]  
numberOfGuests = 6
print("epsilon solution", maximumAreaServingCake(radii, numberOfGuests))
# Output: 7.0686

# Example 2.
radii = [4, 3, 3] 
numberOfGuests = 3
print("epsilon solution", maximumAreaServingCake(radii, numberOfGuests))
# Output: 28.2743

# Example 3.
radii = [6, 7] 
numberOfGuests = 12
print("epsilon solution",maximumAreaServingCake(radii, numberOfGuests))
# Output: 21.9911


# similar problems:
#     https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
#     and knapsack