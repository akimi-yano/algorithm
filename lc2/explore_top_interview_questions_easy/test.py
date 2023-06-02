'''
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, 
so return 964176192 which its binary representation is 00111001011110000010100101000000
'''
n = 43261596
print(n)
# print(bin(n))

chars = bin(n)

ans = []
for c in chars[-1:1:-1]:
    ans.append(c)

for _ in range(6):
    ans.append('0')

string = "".join(ans)
print(string)
print(int(string,2))