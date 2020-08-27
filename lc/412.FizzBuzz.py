# 412. Fizz Buzz

# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

# Example:

# n = 15,

# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]


# This solution works ! 
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for num in range(1,n+1):
            if num%3 == 0 and num%5 == 0:
                ans.append("FizzBuzz")
            elif num%3 == 0:
                ans.append("Fizz")
            elif num%5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(num))
        return ans 

# This solution also works - 7 months ago 
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = []
        for i in range (1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                a.append("FizzBuzz")
            elif i % 3 == 0:
                a.append("Fizz")
            elif i % 5 == 0:
                a.append("Buzz")
            else:
                a.append(str(i))
        return a
    
# One liner solution :)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [str(i) if (i%3!=0 and i%5!=0) else (('Fizz'*(i%3==0)) + ('Buzz'*(i%5==0))) for i in range(1,n+1)]