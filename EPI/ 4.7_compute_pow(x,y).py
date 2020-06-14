# [In Progress]
# 4.7_compute_pow(x,y)
# write a program that takes a double x and an integer y and returns x^y.
# You can ignore overflow and underflow.

# underflow: the generation of a number that is too small to be represented in the device meant to store it.
# overflow: the generation of a number or some other data item that is too large for an assigned location or memory space.
def pow(x,y):
    return x**y
    
print(pow(2.5,2))