def check(n):
    print("original number: ", n)
    print("binary rep of original number: ", bin(n))
    print("LSB = find right most bit that is 1: ", bin(n & -n))
    print("flip 1 to 0: ", bin(n & (n-1)))
    print("*"*50)
for i in range(10):
    check(i)