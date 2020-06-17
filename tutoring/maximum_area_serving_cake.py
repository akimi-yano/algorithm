# Maximum Area Serving Cake

# Last Edit: September 23, 2019 12:44 PM

# Given an array containing the radii of circular cakes and the number of guests, determine the largest piece that can be cut from the cakes such that every guest gets a piece of the cake with the same area. It is not possible that a single piece has some part of one cake and some part of another cake and each guest is served only one piece of cake.

# Example 1:

# Input: radii = [1, 1, 1, 2, 2, 3],  numberOfGuests = 6.
# Output: 7.0686
# Explanation:
# Reason being you can take the area of the cake with a radius of 3, and divide by 4. (Area  28.743 / 4  = 7.0686)
# Use a similary sized piece from the remaining cakes of radius 2 because total area of cakes with radius 2 are > 7.0686
# Example 2:

# Input: radii = [4, 3, 3], numberOfGuests = 3
# Output: 28.2743
# Example 3:

# Input: radii = [6, 7], numberOfGuests = 12
# Output: 21.9911