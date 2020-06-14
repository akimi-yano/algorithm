# [In Progress]
# 4.8_reverse_digits
# write a program which takes an integer and returns the integer corresponding to the digits of the
# input written in reverse order.
# For example, the reverse of 42 is 24, and the reverse of 314 is 413.

def reverse_digits(num):
    ans =""
    ans += str(num%10)
    ans += str(num//10)
  
    return int(ans)
# print(reverse_digits(42)) 
print(reverse_digits(314))