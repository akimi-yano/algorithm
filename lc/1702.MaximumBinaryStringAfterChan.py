# 1702. Maximum Binary String After Change
# Medium

# 62

# 6

# Add to List

# Share
# You are given a binary string binary consisting of only 0's or 1's. You can apply each of the following operations any number of times:

# Operation 1: If the number contains the substring "00", you can replace it with "10".
# For example, "00010" -> "10010"
# Operation 2: If the number contains the substring "10", you can replace it with "01".
# For example, "00010" -> "00001"
# Return the maximum binary string you can obtain after any number of operations. Binary string x is greater than binary string y if x's decimal representation is greater than y's decimal representation.

 

# Example 1:

# Input: binary = "000110"
# Output: "111011"
# Explanation: A valid transformation sequence can be:
# "000110" -> "000101" 
# "000101" -> "100101" 
# "100101" -> "110101" 
# "110101" -> "110011" 
# "110011" -> "111011"
# Example 2:

# Input: binary = "01"
# Output: "01"
# Explanation: "01" cannot be transformed any further.
 

# Constraints:

# 1 <= binary.length <= 105
# binary consist of '0' and '1'.


# this approach does not work 

# class Solution:
#     def maximumBinaryString(self, binary: str) -> str:
#         binary = list(binary)
        
#         while True:
#             changedA = False
#             changedB = False
            
#             for i in range(len(binary)-1):
#                 if binary[i] == '0' and binary[i+1] == '0':
#                     binary[i] = '1'
#                     changedA = True
            
#             if not changedA:
#                 for i in range(len(binary)-2, -1, -1):
#                     if binary[i] == '1' and binary[i+1] == '0':
#                         binary[i] = '0'
#                         binary[i+1] = '1'
#                         changedB = True
        
#             if not changedA and not changedB:
#                 break
            
#         return "".join(binary)


# this approach does not work 

# class Solution:
#     def maximumBinaryString(self, binary: str) -> str:
#         best = int(binary, base=2)
#         binary = list(binary)      
        
#         # while True:
#         #     changedA = False
#         #     changedB = False
            
#         for i in range(len(binary)-1):
#             if binary[i] == '0' and binary[i+1] == '0':
#                 binary[i] = '1'
#                 changedA = True
            
# #             if not changedA:
# #                 temp = binary
# #                 for i in range(len(temp)-2, -1, -1):
# #                     if temp[i] == '1' and temp[i+1] == '0':
# #                         temp[i] = '0'
# #                         temp[i+1] = '1'
# #                         changedB = True
# #                         break
# #                 newtemp = int("".join(temp))
# #                 if newtemp > best:
# #                     best  = newtemp
# #                     binary = temp
            
# #             if not changedA and not changedB:
#                 # break
            
#         return "".join(binary)


# this approach does not work 

# class Solution:
#     def maximumBinaryString(self, binary: str) -> str:
        
#         best = int(binary, base=2)
#         binary = list(binary)  
        
#         def helper(i, best):
#             if i >= len(binary)-1:
#                 return int("".join(binary), base=2)
            
#             if binary[i] == '0' and binary[i+1] == '0':
#                 binary[i] = '1'
#                 if  helper(i+1, best) < best:
#                     binary[i] = '0'
                
#             if  binary[i] == '1' and binary[i+1] == '0':
#                 binary[i] = '0'
#                 binary[i+1] = '1'
#                 if helper(i+1, best) < best:
#                     binary[i] = '1'
#                     binary[i+1] = '0'
                
#             return best
#         return bin(helper(0, best))[2:].zfill(len(binary))
        
        
# This solution works !

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # greedy have as many 1 as possible on the left
        # if there are more than 1 0s, its worth swapping from 10 to 01 so that it becomes from 00 to 10
        if '0' not in binary:
            return binary
        
        ans = []
        idx = binary.index('0')
        
        for i in range(idx):
            ans.append('1')
        
        ones = 0
        zeros = 0
        for i in range(idx, len(binary)):
            if binary[i] == '0':
                zeros += 1
            else:
                ones += 1
        
        while zeros >= 2:
            zeros -= 1
            ans.append('1')
        ans.append('0')
        
        while ones >= 1:
            ones -= 1
            ans.append('1')

        return "".join(ans)
        


# This solution works ! - optimization

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        zeros = Counter(binary)['0']
        if zeros < 2:
            return binary
        start_idx = binary.index('0')
        return '1' * (start_idx + zeros-1) + '0' + '1' * (len(binary) - (start_idx + zeros))
    
        # greedy have as many 1 as possible on the left
        # if there are more than 1 0s, its worth swapping from 10 to 01 so that it becomes from 00 to 10

        