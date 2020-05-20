# 406 - Trapping Rain Water

# Given an array arr[] of N non-negative integers representing height of 
# blocks at index i as Ai where the width of each block is 1. 
# Compute how much water can be trapped in between blocks after raining.



# ex)
# Input: [3, 0, 2, 0, 4]      
# Output: 7

# Basic Insight:
# An element of the array can store water if there are higher bars on left and right. 
# The amount of water to be stored in every element can be found out by finding the heights of bars on the left and right sides. 
# The idea is to compute the amount of water that can be stored in every element of the array.


# Constraints
#                                  Advanced			 Insane
# Time Complexity:			        O(N)				O(N)
# Auxiliary Space Complexity: 		O(N)				O(1)

# Solution
# Instantiate an integer total to track rain water.
# Create an array called max_left to track the maximum height to the left of each index, and populate that array.
# The example above would be: [0, 3, 3, 3, 3]
# Also create an array called max_right to track the maximum height to the right of each index, and populate that array
# The example above would be: [4, 4, 4, 4, 0]
# Loop through the input array with index i At each index, subtract the current value from the lower of the left_max and right_max If the result is greater than zero, add it to the total Return total at the end.
# Resources: https://www.geeksforgeeks.org/trapping-rain-water/



# Method 1: This is a simple solution to the above problem.

# Approach: The idea is to traverse every array element and find the highest bars on left and right sides. Take the smaller of two heights. The difference between the smaller height and height of the current element is the amount of water that can be stored in this array element.
# Algorithm:
# 1. Traverse the array from start to end.
# 2. For every element, traverse the array from start to that index and find the maximum height (a) and traverse the array from the current index to end and find the maximum height (b).
# 3. The amount of water that will be stored in this column is min(a,b) – array[i], add this value to total amount of water stored
# 4. Print the total amount of water stored.

# Function to return the maximum  
# water that can be stored  

# Complexity Analysis:
# Time Complexity: O(n2).
# There are two nested loops traversing the array, So time Complexity is O(n2).
# Space Complexity: O(1).
# No extra space required.
# def maxWater(arr) : 
#     # To store the maximum water  
#     # that can be stored  
#     res = 0;  
#     # For every element of the array  
#     for i in range(1, len(arr)-1) :  
    
#         # Find the maximum element on its left  
#         left = arr[i]  
#         for j in range(i) : 
#             left = max(left, arr[j]);  
#         # Find the maximum element on its right  
#         right = arr[i]  
#         for j in range(i + 1 , len(arr)) :  
#             right = max(right, arr[j])               
#         # Update the maximum water 
#         res = res + (min(left, right) - arr[i])
#     return res  
# print(maxWater([3,0,2,0,4]))

# Method 2: This is an efficient solution to the above problem.

# Approach: In the previous solution, to find the highest bar on the left and right, array traversal is needed which reduces the efficiency of the solution. To make this efficient one must pre-compute the highest bar on the left and right of every bar in linear time. Then use these pre-computed values to find the amount of water in every array element.
# Algorithm:
# 1. Create two array left and right of size n. create a variable max_ = INT_MIN.
# 2. Run one loop from start to end. In each iteration update max_ as max_ = max(max_, arr[i]) and also assign left[i] = max_
# 3. Update max_ = INT_MIN.
# 4. Run another loop from end to start. In each iteration update max_ as max_ = max(max_, arr[i]) and also assign right[i] = max_
# 5. Traverse the array from start to end.
# 6. The amount of water that will be stored in this column is min(a,b) – array[i],(where a = left[i] and b = right[i]) add this value to total amount of water stored
# 7. Print the total amount of water stored.

# Complexity Analysis:
# Time Complexity: O(n).
# Only one traversal of the array is needed, So time Complexity is O(n).
# Space Complexity: O(n).
# Two extra array is needed each of size n.



# Python program to find maximum amount of water that can 
# be trapped within given set of bars. 
  
def findWater(arr, n): 
  
    # left[i] contains height of tallest bar to the 
    # left of i'th bar including itself 
    left = [0]*n 
  
    # Right [i] contains height of tallest bar to 
    # the right of ith bar including itself 
    right = [0]*n 
  
    # Initialize result 
    water = 0
  
    # Fill left array 
    left[0] = arr[0] 
    for i in range( 1, n): 
        left[i] = max(left[i-1], arr[i]) 
  
    # Fill right array 
    right[n-1] = arr[n-1] 
    for i in range(n-2, -1, -1): 
        right[i] = max(right[i + 1], arr[i]); 
  
    # Calculate the accumulated water element by element 
    # consider the amount of water on i'th bar, the 
    # amount of water accumulated on this particular 
    # bar will be equal to min(left[i], right[i]) - arr[i] . 
    for i in range(0, n): 
        water += min(left[i], right[i]) - arr[i] 
  
    return water 
  
  
# Driver program 
  
arr = [3,0,2,0,4] 
n = len(arr) 
print("Maximum water that can be accumulated is", findWater(arr, n)) 
  
  
# Space Optimization for above Solution: 
# Instead of maintaing two arrays of size n for storing left and right max of each element, 
# maintain two variables to store the maximum till that point. 
# Since water trapped at any element = min(max_left, max_right) – arr[i]. 
# Calculate water trapped on smaller element out of A[lo] and A[hi] first and move the pointers till lo doesn’t cross hi.
# Implementation:

# Python program to find 
# maximum amount of water that can 
# be trapped within given set of bars. 
# Space Complexity : O(1) 


# Complexity Analysis:
# Time Complexity: O(n).
# Only one traversal of the array is needed.
# Auxiliary Space: O(1).
# As no extra space is required.
def findWater(arr, n): 
  
    # initialize output 
    result = 0
       
    # maximum element on left and right 
    left_max = 0
    right_max = 0
       
    # indices to traverse the array 
    lo = 0
    hi = n-1
       
    while(lo <= hi):  
      
        if(arr[lo] < arr[hi]): 
          
            if(arr[lo] > left_max): 
  
                # update max in left 
                left_max = arr[lo] 
            else: 
  
                # water on curr element = max - curr 
                result += left_max - arr[lo] 
            lo+= 1
          
        else: 
          
            if(arr[hi] > right_max): 
                # update right maximum 
                right_max = arr[hi] 
            else: 
                result += right_max - arr[hi] 
            hi-= 1
          
    return result 
   
# Driver program 
  
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] 
n = len(arr) 
  
print("Maximum water that can be accumulated is ", 
        findWater(arr, n)) 
  




  
# Method 3:Here another efficient solution has been shown.

# Approach : The concept here is that if there is a larger wall to the right then the water can be retained with height equal to the smaller wall on the left. If there are no larger walls to the right then start from the left. There must be a larger wall to the left now. Let’s take an example if the heights are {….,3, 2, 1, 4,….}, So here 3 and 4 are boundaries the heights 2 and 1 are submerged and cannot act as boundaries. So at any point or index knowing the previous boundary is sufficient if there is a higher or equal length boundary in the remaining part of the array. If not then traverse the array backwards and now must be a larger wall to the left.
# Algorithm :
    # Loop from index 0 to the end of the given array.
    # If a wall greater than or equal to the previous wall is encountered then make note of the index of that wall in a var called prev_index.
    # Keep adding previous wall’s height minus the current (ith) wall to the variable water.
    # Have a temporary variable that stores the same value as water.
    # If no wall greater than or equal to the previous wall is found then quit.
    # If prev_index < size of the input array then subtract the temp variable from water, and loop from end of the input array to prev_index and find a wall greater than or equal to the previous wall (in this case, the last wall from backwards).
# Implementation


# Pythpn3 implementation of the approach 
  
# Function to return the maximum 
# water that can be stored 
def maxWater(arr, n): 
    size = n - 1
  
    # Let the first element be stored as 
    # previous, we shall loop from index 1 
    prev = arr[0] 
  
    # To store previous wall's index 
    prev_index = 0
    water = 0
  
    # To store the water until a larger wall 
    # is found, if there are no larger walls 
    # then delete temp value from water 
    temp = 0
    for i in range(1, size + 1): 
  
        # If the current wall is taller than 
        # the previous wall then make current 
        # wall as the previous wall and its 
        # index as previous wall's index 
        # for the subsequent loops 
        if (arr[i] >= prev): 
            prev = arr[i] 
            prev_index = i 
  
            # Because larger or same height wall is found 
            temp = 0
        else: 
  
            # Since current wall is shorter than 
            # the previous, we subtract previous 
            # wall's height from the current wall's 
            # height and add it to the water 
            water += prev - arr[i] 
  
            # Store the same value in temp as well 
            # If we dont find any larger wall then 
            # we will subtract temp from water 
            temp += prev - arr[i] 
  
    # If the last wall was larger than or equal 
    # to the previous wall then prev_index would 
    # be equal to size of the array (last element) 
    # If we didn't find a wall greater than or equal 
    # to the previous wall from the left then 
    # prev_index must be less than the index 
    # of the last element 
    if (prev_index < size): 
  
        # Temp would've stored the water collected 
        # from previous largest wall till the end 
        # of array if no larger wall was found then 
        # it has excess water and remove that 
        # from 'water' var 
        water -= temp 
  
        # We start from the end of the array, so previous 
        # should be assigned to the last element 
        prev = arr[size] 
  
        # Loop from the end of array up to the 'previous index' 
        # which would contain the "largest wall from the left" 
        for i in range(size, prev_index - 1, -1): 
  
            # Right end wall will be definitely smaller 
            # than the 'previous index' wall 
            if (arr[i] >= prev): 
                prev = arr[i] 
            else: 
                water += prev - arr[i] 
  
    # Return the maximum water 
    return water 
  
# Driver code 
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] 
n = len(arr) 
print(maxWater(arr, n)) 

# Complexity Analysis:
# Time Complexity: O(n).
# As only one traversal of the array is needed.
# Auxiliary Space: O(1).
# As no extra space is required.