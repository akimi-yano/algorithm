# 537. Complex Number Multiplication
# Medium

# 416

# 1006

# Add to List

# Share
# A complex number can be represented as a string on the form "real+imaginaryi" where:

# real is the real part and is an integer in the range [-100, 100].
# imaginary is the imaginary part and is an integer in the range [-100, 100].
# i2 == -1.
# Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

 

# Example 1:

# Input: num1 = "1+1i", num2 = "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
# Example 2:

# Input: num1 = "1+-1i", num2 = "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
 

# Constraints:

# num1 and num2 are valid complex numbers.


# This solution works:


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        '''
        (a+bi)*(c+di)
        a*c + a*di + bi*c + bi*di
        i is kyosuu = square root of negative one
        i ** 2 = -1
        a*c + i(a*d+b*c) + -b*d
        a*c - b*d + i(a*d+b*c) this is the formula
        '''
        "1+1i"
        nums1 = num1[:-1]
        ba = []
        cur = 0
        digit = 0
        for i in range(len(nums1)-1,-1,-1):
            if nums1[i] == "+":
                ba.append(cur)
                cur = 0
                digit = 0
            elif nums1[i] == "-":
                cur *= -1
            else:
                cur = cur + int(nums1[i]) * (10 ** digit)
                digit += 1
        
        ba.append(cur)
        b, a = ba[0], ba[1]
        
        
        nums2 = num2[:-1]
        dc = []
        cur = 0
        digit = 0
        for i in range(len(nums2)-1,-1,-1):
            if nums2[i] == "+":
                dc.append(cur)
                cur = 0
                digit = 0
            elif nums2[i] == "-":
                cur *= -1
            else:
                cur = cur+int(nums2[i]) * (10 ** digit)
                digit += 1
        
        dc.append(cur)
        d, c = dc[0], dc[1]

        first = a*c + (-1)*b*d 
        last = a*d + b*c
        return str(first) + "+" + str(last) + "i"