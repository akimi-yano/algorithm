# 233 - Hexadecimal Converter

# Given a positive integer (including 0), convert it to its hexadecimal representation

# Input: n (Integer)
# Output: Str (Hex representation)

# #### Example:

# 0 => '0'
# 1 => '1'
# 2 => '2'
# 3 => '3'

# 9 => '9'
# 10 => 'a'
# 11 => 'b'

# 15 => 'f'
# 16 => '10'

# 30 => '1e'
# 31 => '1f'
# 32 => '20'

# 255 => 'ff'
# 256 => '100'

# # Constraints
# Time Complexity: O(log(N))
# Space Complexity: O(log(N))



# Please use pure recursion to solve this problem.
# Do not use your language's native integer to string converters.



# # Hints:
# Hexadecimal numbers (`0123456789abcdef`) can also be thought of as a base-16
# numbering system. We are most used to the base-10 system (`0123456789`).
# If you received this same sort of integer input, and had to convert it to a
# base-10 number, how would you do so?

# Begin with the smallest cases. What would these be? How could you use this to
# build your base cases for recursion?
