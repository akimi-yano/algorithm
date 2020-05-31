  
  
  
#  /*Given n ropes of different lengths represented by an array of integers, 
# connect them all into a single rope in a way that minimizes the cost of connecting 
# them.
# The cost of connecting two ropes is equal to sum of their lengths. We want to
#  minimize the cost of connecting all the ropes.
# Input: ropes, [Integer]
# Output: Integer

# // // In: [4, 3, 2, 6]
# // // Out: 29
# // // Explanation:

# // // First we connect 3 + 2 = 5, giving the following ropes: [4,5,6]
# // // Then we connect 5 + 4 = 9, giving the following ropes: [9,6]
# // // Then we connect 9 + 6 = 15, giving the final combination of all ropes: [15]

# // // So in total the cost for the most efficient approach is: 5 + 9 + 15 = 29

# // // A less efficient way would be:

# // // First we connect 4 + 6 = 10, giving the following ropes: [10,3,2]
# // // Then we connect 10 + 3 = 13, giving the following ropes: [13,2]
# // // Then we connect 13 + 2 = 15, giving the final combination of all ropes: [15]
# // // So in total the cost for the less efficient approach is: 10 + 13 + 15 = 38
# // // Although in both cases we need to make the same number of connections, 
# the costs are different


#             4                         2                        5                3
#      3       2                3           4             3         4         5       4
# 5                          5             

#                           2 , 3, 4, 5 ----    5,3,4,  2               6,4  5
# */

# //child1 -- 2*parent + 1
# //child2 -- child1+1

# // parent -- child1-1/2 

# def heapify(arr):
  
#   left = 2
  
  
  