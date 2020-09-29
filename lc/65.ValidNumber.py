# 65. Valid Number
# Hard

# 768

# 5059

# Add to List

# Share
# Validate if a given string can be interpreted as a decimal number.

# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false

# Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up 
# front before implementing one. However, here is a list of characters that can be in a valid decimal number:

# Numbers 0-9
# Exponent - "e"
# Positive/negative sign - "+"/"-"
# Decimal point - "."
# Of course, the context of these characters also matters in the input.

# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your function signature accepts a const 
# char * argument, please click the reload button to reset your code definition.




# This solution works !:

class Solution:
    def isNumber(self, s: str) -> bool:
        
        try: 
            maybe_float = float(s)
            return type(maybe_float) == float
            
        except:
            return False
        



# Regex solution: 
import re
class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = '\s*([+-]?((\d*\.\d+)|(\d+\.?\d*))(e[+-]?\d+)?)\s*'
        return re.fullmatch(pattern,s)
    
    
    

# This approach does not work :
# class Solution:
    # def isNumber(self, s: str) -> bool:
    #     try: 
    #         maybe_float = float(s)
    #         return type(maybe_float) == float      
    #     except:
    #         return False
    
    # def isNumber(self, s: str) -> bool:
    #     pattern = '\s*([+-]?((\d*\.\d+)|(\d+\.?\d*))(e[+-]?\d+)?)\s*'
    #     return re.fullmatch(pattern,s)
    '''
    TRUE: 
    "0"
    " 0.1 "
    "53.5e93" 
    "2e10" 
    " -90e3   " 
    " 6e-1"

    FALSE:
    " 1e"
    "e3" 
    " 99e2.5 "
    " --6 "
    "-+3" 
    "95a54e53" 
    "abc" 
    "1 a" 
    '''
    '''
    Numbers: 0-9
    Exponent: "e"
    Positive/negative sign: "+" or "-"
    Decimal point: "."
    # '''

    # def isNumber(self, s: str) -> bool:
    #     NUMS  = set([str(i) for i in range(10)])
    #     s =  s.strip()
    #     sign = None
    #     sign_idx = -1
    #     expo = -1
    #     num = -1
    #     point = -1
    #     if len(s) < 1:
    #         return False
    #     for i, elem in enumerate(s):
    #         if elem == ' ':
    #             return False
    #         if elem  == '+':
    #             if not sign:
    #                 sign = "+"
    #                 sign_idx = i
    #                 if i != 0 and i!=expo+1:
    #                     return False
    #             else:
    #                 return False
    #         elif elem  == '-':
    #             if not sign:
    #                 sign = "-" 
    #                 sign_idx = i
    #                 if i != 0 and i!=expo+1:
    #                     return False
    #             else:
    #                 return False
    #         if elem == 'e':
    #             if expo == -1:
    #                 expo = i
    #                 if num == -1:
    #                     return False
    #             else:
    #                 return False
    #         if elem in NUMS:
    #             num = i
    #         if elem == '.' and expo>-1:
    #             return False
    #         if elem == '.':
    #             if point == -1:
    #                 point = i
    #             else:
    #                 return False
    #         if elem not in NUMS and elem != 'e' and elem !='.' and elem not in ["+","-"]:
    #             return False
            
    #     if num == -1:
    #         return False
    #     if num<expo:
    #         return False
    #     if sign_idx == point-1:
    #         return False
    #     return True
            
                
                
                
                
# THIS SOLUTION WORKS !
class Solution:
    NUMS = set([chr(ord('0')+ i) for i in range(10)])
    def isNumber(self, s: str) -> bool:
        elems1 = s.strip().split('e')

        # before the e
        num = elems1[0]
        if len(num) < 1:
            return False
        
        # check for signs
        if num[0] not in Solution.NUMS and num[0] != '.':
            sign, num = num[0], num[1:]
            if sign not in ['+', '-']:
                return False

        elems2 = num.split('.')
        
        hasnumber = False
        
        # before the dot
        whole = elems2[0]
        if len(whole) > 0:
            hasnumber = True
            for c in whole:
                if c not in Solution.NUMS:
                    return False

        # after the dot
        if len(elems2) == 2:
            fraction = elems2[1]
            if len(fraction) > 0:
                hasnumber = True
            for c in fraction:
                if c not in Solution.NUMS:
                    return False
        if not hasnumber:
            return False

        # too many dots
        if len(elems2) > 2:
            return False
        
        # exponent
        if len(elems1) == 2:
            exponent = elems1[1]
            if len(exponent) < 1:
                return False
            # check for signs
            if exponent[0] not in Solution.NUMS:
                sign, exponent = exponent[0], exponent[1:]
                if sign not in ['+', '-']:
                    return False
            if len(exponent) < 1:
                return False
            for c in exponent:
                if c not in Solution.NUMS:
                    return False
        
        if len(elems1) > 2:
            return False
        
        return True
    
    
    

'''
We use three flags: met_dot, met_e, met_digit, mark if we have met ., 
e or any digit so far. First we strip the string, then go through each char and make sure:

If char == + or char == -, then prev char (if there is) must be e
. cannot appear twice or after e
e cannot appear twice, and there must be at least one digit before and after e
All other non-digit char is invalid

'''

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        met_dot = met_e = met_digit = False
        for i, char in enumerate(s):
            if char in ['+', '-']:
                if i > 0 and s[i-1] != 'e':
                    return False
            elif char == '.':
                if met_dot or met_e: return False
                met_dot = True
            elif char == 'e':
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False
            elif char.isdigit():
                met_digit = True
            else:
                return False
        return met_digit