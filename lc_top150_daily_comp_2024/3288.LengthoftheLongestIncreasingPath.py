'''
3288. Length of the Longest Increasing Path
Hard
Companies
Hint
You are given a 2D array of integers coordinates of length n and an integer k, where 0 <= k < n.

coordinates[i] = [xi, yi] indicates the point (xi, yi) in a 2D plane.

An increasing path of length m is defined as a list of points (x1, y1), (x2, y2), (x3, y3), ..., (xm, ym) such that:

xi < xi + 1 and yi < yi + 1 for all i where 1 <= i < m.
(xi, yi) is in the given coordinates for all i where 1 <= i <= m.
Return the maximum length of an increasing path that contains coordinates[k].

 

Example 1:

Input: coordinates = [[3,1],[2,2],[4,1],[0,0],[5,3]], k = 1

Output: 3

Explanation:

(0, 0), (2, 2), (5, 3) is the longest increasing path that contains (2, 2).

Example 2:

Input: coordinates = [[2,1],[7,0],[5,6]], k = 2

Output: 2

Explanation:

(2, 1), (5, 6) is the longest increasing path that contains (5, 6).

 

Constraints:

1 <= n == coordinates.length <= 105
coordinates[i].length == 2
0 <= coordinates[i][0], coordinates[i][1] <= 109
All elements in coordinates are distinct.
0 <= k <= n - 1
'''

class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        def get_longest_length_of_strictly_increasing_list(arr):
            '''
            [1,7],[1,4],[6,7],[6,4]
            its important to sort the y in a reversed order to make sure that we do not use the 
            same x values again - as in using monoque, we are going to override the value
            also - only push the y value into monoqueue
            '''
            monoqueue = []
            largest_length = 0
            for _, y2 in arr:
                idx = bisect_left(monoqueue, y2)
                if idx <= len(monoqueue)-1:
                    monoqueue[idx] = y2
                else:
                    monoqueue.append(y2)
                largest_length = max(largest_length, len(monoqueue))
            return largest_length

        x, y = coordinates[k]
        larger_than_k = []
        smaller_than_k = []
        for x1, y1 in coordinates:
            if x1 > x and y1 > y:
                larger_than_k.append([x1, y1])
            elif x1 < x and y1 < y:
                smaller_than_k.append([x1, y1])
        larger_than_k.sort(key=lambda x : (x[0], -x[1]))
        smaller_than_k.sort(key=lambda x : (x[0], -x[1]))
        larger_side = get_longest_length_of_strictly_increasing_list(larger_than_k)
        smaller_side = get_longest_length_of_strictly_increasing_list(smaller_than_k)
        return smaller_side + 1 + larger_side
