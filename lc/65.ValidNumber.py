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
            
                
                
                
                
        