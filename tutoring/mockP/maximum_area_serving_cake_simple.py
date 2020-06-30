# Maximum Area Serving Cake

# Given an array containing the radii of circular cakes and the number of guests, 
# determine the largest piece that can be cut from the cakes such that every guest 
# gets a piece of the cake with the same area. It is not possible that a single 
# piece has some part of one cake and some part of another cake and each guest is 
# served only one piece of cake.

# Example 1:

# Input: radii = [1, 1, 1, 2, 2, 3],  numberOfGuests = 6.
# Output: 7.0686

# Explanation:
# Reason being you can take the area of the cake with a radius of 3, and divide by 4. 
# (Area  28.743 / 4  = 7.0686)
# Use a similary sized piece from the remaining cakes of radius 2 because total area 
# of cakes with radius 2 are > 7.0686

# Example 2:

# Input: radii = [4, 3, 3], numberOfGuests = 3
# Output: 28.2743

# Example 3:

# Input: radii = [6, 7], numberOfGuests = 12
# Output: 21.9911

# def max_area_serving_cake(radii,numberOfGuests):
#     pass

# print(max_area_serving_cake([1, 1, 1, 2, 2, 3],6))
import math

EPSILON = 0.00001

def can_cut(sizes, to_cut, remaining_guests):
    if remaining_guests < 1:
        return True
    if len(sizes) < 1:
        return False
    
    # try taking a piece from the last cake
    after_cut = sizes[-1] - to_cut
    # if the size of the last cake becomes less than zero, it was too small. throw it away.
    if after_cut < 0:
        sizes.pop()
        return can_cut(sizes, to_cut, remaining_guests)
    # otherwise, udpate the last cake size and the number of remaining guests
    else:
        sizes[-1] = after_cut
        return can_cut(sizes, to_cut, remaining_guests-1)

def max_area_serving_cake(cakes, guests):
    sizes = [cake**2 for cake in cakes]
    left = 0
    right = sum(sizes) / guests
    
    mid = -1
    while left < right:
        new_mid = (left+right) / 2
        if abs(new_mid-mid) < EPSILON:
            break
        mid = new_mid
        
        # making a copy of the size list because we will modify it
        if can_cut(list(sizes), mid, guests):
            left = mid
        else:
            right = mid
    return round(mid*math.pi, 4)

a = [1, 1, 1, 2, 2, 3]
b = 6
print(max_area_serving_cake(a, b))
a = [4, 3, 3]
b = 3
print(max_area_serving_cake(a, b))
a = [6, 7]
b = 12
print(max_area_serving_cake(a, b))