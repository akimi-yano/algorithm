"""

For this question, please refer to this image of a dart board:
https://upload.wikimedia.org/wikipedia/commons/5/57/Dartboard_diagram.svg

Although, for the purpose of this question, we will ignore the "inner bullseye" and
"outer bullseye." What remains are 20 segments, numbered from 1 to 20 (shuffled, but all
present) and two rings: outer and inner.

If a dart lands in the section of a segment that does not intersect a ring, it scores points
equal to that segment's number. If it lands in the outer ring, it scores double the segment's value,
and if in the inner ring, triple the value. Thus, there are 60 different ways to score (although some
of them share a value).

One way to play darts is to be given some target number and to try and score exactly that many points
with up to three darts. Some targets are impossible to reach, such as any number greater than 180 (since
the maximum score per-dart is 60), but also some smaller numbers, such as 179 and 157. All other
targets have at least one solution, and most have many solutions.

For example, the target 1 has just one solution:

[(1x1)]

As does 180:

[(20x3, 20x3, 20x3)]

The target 3 has 5 solutions:

[(1x1, 1x1, 1x1), (1x2, 1x1), (2x1, 1x1), (1x3), (3x1)]

10 has 54 solutions, 20 has 212 solutions, and 54 has the most with 619 solutions.

I'd like you to write a function that takes a target number as input, and returns a list of all one-,
two-, or three-dart solutions for that target.

"""


'''
input: integer 
output: [(1x1)]
x3 = triple 
invalid -> [] empty


triple x3
double x2
other x1

1-20
3 shots 

60 different ways
more than 180 is impossible
maximum score per-dart is 60 ( 20 x3)

target 180
1x1=1
179 180
[["1x1", 1]]

steps:
1 prepopulate all options []
2 recusively explore each option - index, remaining, arr
3 basecase1: remaining == 0 return sequence -> arr 
4 basecase2: remaining < 0: return []
5 2 options: use or not use
6 make sure 3 shots 


'''

def get_options(target):
    options = []

    for num in range(1, 21):
        for mult in range(1, 4):
            options.append((num*mult, str(num)+"x"+str(mult)))
    
    def helper(i, remaining, arr, shots):
        if remaining == 0:
            return [arr]
        if i > len(options)-1 or remaining < 0 or shots <=0:
            return []
        
        ans =[]
        # use
        ans.extend(temp for temp in helper(i, remaining - options[i][0], arr + [options[i][1]], shots-1))
        # not use
        ans.extend(temp for temp in helper(i+1, remaining, arr, shots))
        return ans
        
    return helper (0, target, [], 3)
    
                           
print(get_options(3))
print(get_options(180))
answer = get_options(20) 
print(answer, len(answer))
answer = get_options(10) 
print(answer, len(answer))
answer = get_options(54) 
print(len(answer))