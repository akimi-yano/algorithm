# 539. Minimum Time Difference

# Given a list of 24-hour clock time points in "Hour:Minutes" format, 
# find the minimum minutes difference between any two time points in the list.
# Example 1:
# Input: ["23:59","00:00"]
# Output: 1

# Note:
# The number of time points in the given list is at least 2 
# and won't exceed 20000.
# The input time is legal and ranges from 00:00 to 23:59.


# convert time to minutes? maybe.
# 0 1 : 3 4
# int(index 0 + 1) * 60  + int(index 3 + 4)
# int(string[0] + string[1]) 
# sort after conversion?


# 1 convert hour to minutes
# 2 sort 
# 3 iterate and compare 2 elements 
# 4 go back to beginning and comapre with the beginning

def findMinDifference(timePoints):
  arr = []
  for time in timePoints:
      arr.append(int(time[0] + time[1])*60 + int(time[3] + time[4]))
  
  arr.sort()
  
  min_diff = abs((arr[0]+1440)-arr[-1])
  
  for i in range(len(arr)-1):
    min_diff = min(min_diff, abs(arr[i]-arr[i+1]))
    
  return min_diff

print(findMinDifference(["23:59","00:00"]))
# --------------------> ??
# [5,100,250,300,1439]
# 6 (minute)
