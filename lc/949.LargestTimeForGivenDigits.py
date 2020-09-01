# 949. Largest Time for Given Digits

# Given an array of 4 digits, return the largest 24 hour time that can be made.

# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

# Return the answer as a string of length 5.  If no valid time can be made, return an empty string.


# Example 1:

# Input: [1,2,3,4]
# Output: "23:41"
# Example 2:

# Input: [5,5,5,5]
# Output: ""

# Note:

# A.length == 4
# 0 <= A[i] <= 9

# This solution works !
# I created all the options recursively and iterated through all the options and got the largest in time !

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:

        self.hmax = 23
        self.hmin = 0
        self.mmax = 59
        self.mmin = 0
 
        def helper(arr):
            if len(arr) <= 1:
                return [arr]
            temp = []
            for i in range(len(arr)):
                array = helper(arr[:i]+arr[i+1:])
                for ta in array:
                    temp.extend([[arr[i]]+ ta])    
            return temp
        options = helper(A)
        best_h = float('-inf')
        best_m = float('-inf')
        for option in options:
            h = int(''.join([str(elem) for elem in option[:2]]))
            m = int(''.join([str(elem) for elem in option[2:]]))
            # print(h,m)
            if self.hmin<=h<=self.hmax and self.mmin<=m<=self.mmax and h>=best_h:
                if h>best_h:
                    best_h = h 
                    best_m = m
                elif m>=best_m:
                    best_m = m
                    
        if best_h != float('-inf') and best_m != float('-inf'):
            temph = str(best_h)
            if len(temph)<2:
                temph = "0" + temph
            tempm = str(best_m)
            if len(tempm)<2:
                tempm = "0" + tempm
            return temph + ':' + tempm 
        else:
            return ""

# Another solution :

    def largestTimeFromDigits(self, A):
        return max(["%d%d:%d%d" % t for t in itertools.permutations(A) if t[:2] < (2, 4) and t[2] < 6] or [""])
    
    
# Another ways:

    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = ''
        for i, a in enumerate(A):
            for j, b in enumerate(A):
                for k, c in enumerate(A):
                    if i == j or i == k or j == k:
                        continue
                    hour, minute = str(a) + str(b), str(c) + str(A[6 - i - j - k])
                    if hour < '24' and minute < '60':
                        ans = max(ans, hour + ':' + minute)
        return ans
Use Python lib:

    def largestTimeFromDigits(self, A: List[int]) -> str:
        for time in itertools.permutations(sorted(A, reverse=True)):
            if time[:2] < (2, 4) and time[2] < 6:
                return '%d%d:%d%d' % time
        return ''
    