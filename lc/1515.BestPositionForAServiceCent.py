# 1515. Best Position for a Service Centre

# A delivery company wants to build a new service centre in a new city. The company knows the positions of all the customers in this city on a 2D-Map and wants to build the new centre in a position such that the sum of the euclidean distances to all customers is minimum.

# Given an array positions where positions[i] = [xi, yi] is the position of the ith customer on the map, return the minimum sum of the euclidean distances to all customers.

# In other words, you need to choose the position of the service centre [xcentre, ycentre] such that the following formula is minimized:


# Answers within 10^-5 of the actual value will be accepted.



# Example 1:


# Input: positions = [[0,1],[1,0],[1,2],[2,1]]
# Output: 4.00000
# Explanation: As shown, you can see that choosing [xcentre, ycentre] = [1, 1] will make the distance to each customer = 1, the sum of all distances is 4 which is the minimum possible we can achieve.
# Example 2:


# Input: positions = [[1,1],[3,3]]
# Output: 2.82843
# Explanation: The minimum possible sum of distances = sqrt(2) + sqrt(2) = 2.82843
# Example 3:

# Input: positions = [[1,1]]
# Output: 0.00000
# Example 4:

# Input: positions = [[1,1],[0,0],[2,0]]
# Output: 2.73205
# Explanation: At the first glance, you may think that locating the centre at [1, 0] will achieve the minimum sum, but locating it at [1, 0] will make the sum of distances = 3.
# Try to locate the centre at [1.0, 0.5773502711] you will see that the sum of distances is 2.73205.
# Be careful with the precision!
# Example 5:

# Input: positions = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]
# Output: 32.94036
# Explanation: You can use [4.3460852395, 4.9813795505] as the position of the centre.


# Constraints:

# 1 <= positions.length <= 50
# positions[i].length == 2
# 0 <= positions[i][0], positions[i][1] <= 100


# FORMULA for geometric median - ml
# https://en.wikipedia.org/wiki/Geometric_median

class Solution:
	def getMinDistSum(self, positions: List[List[int]]) -> float:

		x, y = None, None

		x_sum, y_sum = 0, 0
		for x, y in positions:
			x_sum += x
			y_sum += y

		x = x_sum / len(positions)
		y = y_sum / len(positions)

		def dis(a, b):
			return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

		prex, prey = float('-inf'), float('-inf')
		delte = 1 / (10 ** 9)

		while dis((x, y), (prex, prey)) > delte:
			upx, downx, upy, downy = 0, 0, 0, 0
			for px, py in positions:
				temp = dis((px, py), (x, y))
				if temp == 0:
					continue
				else:
					upx += px / temp
					downx += 1 / temp
					upy += py / temp
					downy += 1 / temp
			if downx == 0 and downy == 0:
				break
			if downx != 0:
				newx = upx/downx
			if downy != 0:
				newy = upy/downy
			prex, prey, x, y = x, y, newx, newy            

		res = 0
		for a, b in positions:
			res += math.sqrt((a - x) ** 2 + (b - y) ** 2)

		return res


# This problem is to compute a quantity called "geometric median". There are algorithms dedicated to solve such problems such as Weiszfeld's algorithm. But those algorithms leverages on statistical routines such as weighted least squares.

# Since this is a 2d toy problem, we could use some "brute force" grid searching method to find an approximation. Suppose you think x, y is a candidate. Then, you could perturb the point along x and y by a small amount (chg in the implementation) and check if the new point provides a smaller distance. If so, the new point becomes the new candidate.

# The trick is to progressively decrease chg to a satisfying precision (1e-5 in this setting). One could reduce it by half or any chosen factor. In the meantime, centroid is a good starting point.

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        #euclidean distance 
        fn = lambda x, y: sum(sqrt((x-xx)**2 + (y-yy)**2) for xx, yy in positions)
        #centroid as starting point
        x = sum(x for x, _ in positions)/len(positions)
        y = sum(y for _, y in positions)/len(positions)
        
        ans = fn(x, y)
        chg = 100 #change since 0 <= positions[i][0], positions[i][1] <= 100
        while chg > 1e-6: #accuracy within 1e-5
            zoom = True
            for dx, dy in (-1, 0), (0, -1), (0, 1), (1, 0):
                xx = x + chg * dx
                yy = y + chg * dy
                dd = fn(xx, yy)
                if dd < ans: 
                    ans = dd 
                    x, y = xx, yy
                    zoom = False 
                    break 
            if zoom: chg /= 2
        return ans 
    
    
# the fast and brute force solution (I like ) using a storategy like binary search
class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def euclidean(x, y):
            return sum([((x-p[0])**2+(y-p[1])**2)**0.5 for p in positions])
        
        # start at the average point (sum/count)
        xc = sum([p[0] for p in positions])/len(positions)
        yc = sum([p[1] for p in positions])/len(positions)
        error = euclidean(xc, yc)
        
        # use multiplier (<=100) to move the 4 indices equally
        multiplier = 100
        # epsilon is 10^-5 = 0.00001 so use 10^6 = 0.000001
        epsilon = 0.000001
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while multiplier > epsilon:
            x_best, y_best, error_best = xc, yc, error
            for d in directions:
                x_new, y_new = xc + d[0]*multiplier, yc + d[1]*multiplier
                error_new = euclidean(x_new, y_new)
                if error_new < error_best:
                    x_best, y_best, error_best = x_new, y_new, error_new
            # divide it by 2 (like binary search) only if the points stop moving
            if (x_best, y_best) == (xc, yc):
                multiplier /= 2
            else:
                xc, yc, error = x_best, y_best, error_best
        return error