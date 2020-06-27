# Think like a programmer Chapter 2

# PROBLEM 1: HALF OF A SQUARE

# Write a program that uses only two output statements, cout << "#" and cout << "\n",
# to produce a pattern of hash symbols shaped like half of a perfect 5 x 5 square (or a
# right triangle):
    
    
#####
####
###
##
#



'''
#####\n
####\n
###\n
##\n
#\n
'''

'#'
'\n'

def half_square():
    ans = ''
    for i in range(5,0,-1):
        ans+='#'*i
        ans+='\n'
    return ans
print(half_square())

# i 5 4 3 2 1 0
# ans #####\n####\n###\n##\n#\n


# PROBLEM 2: COUNT DOWN BY COUNTING UP
# Write a line of code that goes in the designated position in the loop in the listing

# below. The program displays the numbers 5 through 1, in that order, with each num-
# ber on a separate line.

# for (int row = 1; row <= 5; row++) {
# cout <<  expression << "\n";
# }



def print_reverse():
    for i in range(1, 6):
        # print something here
        print(6-i)
print_reverse()

# Expected output:
#5
#4
#3
#2
#1

print('\n')


# PROBLEM 3: A SIDEWAYS TRIANGLE

# Write a program that uses only two output statements, cout << "#" and cout << "\n",
# to produce a pattern of hash symbols shaped like a sideways triangle:


#
##
###
####
###
##
#




# constraint: you can only modify the string with:
# a) s += "#"
# b) s += "\n"



#
##
###
####
###
##
#


def sideway_triangle():
    res = ''
    for t in range(1,5):
        for k in range(t):
            res+='#'
        res+='\n'
    for j in range(3,0,-1):
        for s in range(j):
            res+='#'
        res+='\n'
    return res
print(sideway_triangle())


def smart_way():
    A = ''
    for row in range(1,8):
        for _ in range(4-(abs(4-row))):
            A+="*"
        A+="\n"
    return A

print(smart_way())


# PROBLEM 4: LUHN CHECKSUM VALIDATION

# The Luhn formula is a widely used system for validating identification numbers. Using
# the original number, double the value of every other digit. Then add the values of the

# individual digits together (if a doubled value now has two digits, add the digits indi-
# vidually). The identification number is valid if the sum is divisible by 10.

# Write a program that takes an identification number of arbitrary length and
# determines whether the number is valid under the Luhn formula. The program must
# process each character before reading the next one.

def luhn_formula(id_num):
    # double the value of every other digit

    new_num = ''
    while id_num !=0:
        new_num += str(id_num%10)
        id_num = id_num//10

        new_num += str((id_num%10)*2)
        id_num = id_num//10
    # print(new_num)
    # get sum 
    suma = 0
    for u in range(len(new_num)):
        suma += int(new_num[u])    
    # print(suma)
    # devide by 10
    return suma%10==0
print(luhn_formula(176248))
# 176248
