# 1360. Number of Days Between Two Dates

# Write a program to count the number of days between two dates.

# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.



# Example 1:

# Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1
# Example 2:

# Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15


# Constraints:

# The given dates are valid dates between the years 1971 and 2100.






# This approach dose not work:

# import datetime
# class Solution:
#     def daysBetweenDates(self, date1: str, date2: str) -> int:
#         d1 = date1.split('-')
#         d2 = date2.split('-')
#         date1 = datetime.datetime(list(int(n) for n in d1))
#         date2 = datetime.datetime(list(int(n) for n in d2))
#         print(date1,date2)

# #         if d1>d2:
# #             return self.daysBetweenDates(date2,date1)
        
# #         print(int(d1[0])+int(d1[1])+int(d1[2]))
# #         print(int(d2[0])+int(d2[1])+int(d2[2]))
# #         # y,m,d = abs(int(d1[0])-int(d2[0])),abs(int(d1[1])-int(d2[1])),abs(int(d1[2])-int(d2[2]))
# #         # print(y,m,d)
# # #         ans = y*360 + m*30 + d
# # #         return ans
    
# # # leap year and dates in month 
# # # "2020-01-15"      2020+1+25
# # # "2019-12-31"      2019+12+31








# Approach:

# The input is of type <string>. To use the datetime module, these strings will first be converted into type <date> 
# using datetime.strptime(date_string, format).
# After conversion, the dates are subtracted, i.e. (date2 - date1).days()
# Note:
# abs() must be used when calculating the difference as any of the dates could be bigger than the other.

from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs((datetime.strptime(date2, '%Y-%m-%d').date() - datetime.strptime(date1, '%Y-%m-%d').date()).days)

# Cleaner Version:

from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        M = datetime.strptime(date1, '%Y-%m-%d').date()
        N = datetime.strptime(date2, '%Y-%m-%d').date()
        return abs((N - M).days)
    

# When m=1 or m=2 (January or February), we let m=13 or m=14 and let y decreased by 1. 
# Imagine it is 13th or 14th month of the last year. By doing that, we let the magical formula also work for those two months. 
# (153 * m + 8) // 5 is just a carefully designed way to record the days of each month. 
# More specifically, it is designed to record the difference of days between two months. 
# Suppose we have March 1st and April 1st, (153 * 3 + 8) // 5 = 93 while (153 * 4 + 8) // 5 = 124, 
# the difference is 31 which is the number of days in March. Suppose we have April 1st to May 1st, 
# (153 * 4 + 8) // 5 = 124 and (153 * 5 + 8) // 5 = 154, the difference is now 30 which is the number of days in April. 
# You can also check other months.

# I learned this formula somewhere else before. It is not something to come up with in minutes.

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def f(date):
            y, m, d = map(int, date.split('-'))
            if m < 3:
                m += 12
                y -= 1
            return 365 * y + y // 4 + y // 400 - y // 100 + d + (153 * m + 8) // 5

        return abs(f(date1) - f(date2))
    

# Brute force approach - very intuitive:

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        r1 = self.get_days(date1)
        r2 = self.get_days(date2)
        return abs(r2 - r1)
    
    def leapyear(self, year):
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True
        
    def get_days(self, a_str):
        s = a_str.split('-')
        year, month, day = map(int, s)
        n_leaps = 0
        for i in range(1971, year):
            n_leaps += int(self.leapyear(i))
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 32]
        res =  n_leaps + 365 * (year - 1971) + sum(months[:month]) + day
        if self.leapyear(year) and month > 2:
            res += 1
        return res


# This soluition works and very intuitive:  

class Solution:
    shorter_months = set([4, 6, 9, 11])
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return self.num_days(min(date1, date2), max(date1, date2))
    
    def num_days(self, date1, date2):
        y1, m1, d1 = [int(elem) for elem in date1.split('-')]
        y2, m2, d2 = [int(elem) for elem in date2.split('-')]
        
        total = 0
        # Calculate the difference in year
        while y1 < y2:
            while m1 < 13:
                total += self.days_in_month(y1, m1) - d1 + 1
                m1 += 1
                d1 = 1
            y1 += 1
            m1 = 1
            d1 = 1
        # Calculate the difference in month
        while m1 < m2:
            total += self.days_in_month(y1, m1) - d1 + 1
            m1 += 1
            d1 = 1
        # Calculate the difference in month
        total += d2 - d1
        return total
            
    
    def days_in_month(self, year, month):
        if month == 2:
            if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
                return 29
            return 28
        if month in Solution.shorter_months:
            return 30
        return 31