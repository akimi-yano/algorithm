# 458. Poor Pigs
# Hard

# 509

# 992

# Add to List

# Share
# There are 1000 buckets, one and only one of them is poisonous, while the rest are filled with water. They all look identical. If a pig drinks the poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket is poisonous within one hour?

# Answer this question, and write an algorithm for the general case.

 

# General case:

# If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the poisonous bucket within p minutes? There is exactly one bucket with poison.

 

# Note:

# A pig can be allowed to drink simultaneously on as many buckets as one would like, and the feeding takes no time.
# After a pig has instantly finished drinking buckets, there has to be a cool down time of m minutes. During this time, only observation is allowed and no feedings at all.
# Any given bucket can be sampled an infinite number of times (by an unlimited number of pigs).



# This approach does not work !

# import math
# class Solution:
#     def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
#         time = math.log2(buckets)
#         print(time)
#         penalty = time * minutesToDie 
#         print(penalty)
#         ans = minutesToTest // time
#         print(ans)
#         # print(buckets, minutesToDie, minutesToTest)
        
# '''
# If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the poisonous bucket within p minutes? There is exactly one bucket with poison.
# '''


# This solution works !


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        '''
        Find minimum x such that (T+1)**x >= N
        T = how many times can you do ? 
        N = buckets
        '''
        x = 0
        while (minutesToTest//minutesToDie + 1) ** x < buckets:
            x += 1
        return x
        
   

'''
With 2 pigs, poison killing in 15 minutes, and having 60 minutes, we can find the poison in up to 25 buckets in the following way. Arrange the buckets in a 5×5 square:

 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
Now use one pig to find the row (make it drink from buckets 1, 2, 3, 4, 5, wait 15 minutes, make it drink from buckets 6, 7, 8, 9, 10, wait 15 minutes, etc). Use the second pig to find the column (make it drink 1, 6, 11, 16, 21, then 2, 7, 12, 17, 22, etc).

Having 60 minutes and tests taking 15 minutes means we can run four tests. If the row pig dies in the third test, the poison is in the third row. If the column pig doesn't die at all, the poison is in the fifth column (this is why we can cover five rows/columns even though we can only run four tests).

With 3 pigs, we can similarly use a 5×5×5 cube instead of a 5×5 square and again use one pig to determine the coordinate of one dimension (one pig drinks layers from top to bottom, one drinks layers from left to right, one drinks layers from front to back). So 3 pigs can solve up to 125 buckets.

In general, we can solve up to (⌊minutesToTest / minutesToDie⌋ + 1)pigs buckets this way, so just find the smallest sufficient number of pigs for example like this:

def poorPigs(self, buckets, minutesToDie, minutesToTest):
    pigs = 0
    while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
        pigs += 1
    return pigs
Or with logarithm like I've seen other people do it. That's also where I got the idea from (I didn't really try solving this problem on my own because the judge's solution originally was wrong and I was more interested in possibly helping to make it right quickly).
'''

# another solution using log

# log a b = log b / log a =  log(buckets) / log(turns + 1)
'''
What matters is number of tests T and number of pigs x. Let us ask inverse question: how many states can we generate with x pigs and T tests to cover N scenarios? This is estimation + example problem, where we need to 1) prove, that we can not make N bigger than some number and 2) give an example, where this N is possible.

Estimation: The number of states is exactly (T+1)^x and here is why. For each pig during T tests, it has exactly T+1 states: dies at some test #i, where 1<= i <= T) or still alive eventually. For x pigs, obviously the maximum possible number of states we could have is (T+1)^x since each is independent and one pig can not influence on another one.

Example: From other side, we can construct the example, using (T+1) based numbers: at first test for i-th pig choose all numbers, where i-th digit is 0. If all pigs are dead, we can immediately say what bucket was poisoned. If k pigs are alive, there will be T^k possible options for T-1 days and k pigs, which can be solved, using induction. For better understanding, imaging the special case: let us have x=3 pigs and T=2 tests. Then our plan is the following:

We have 27 different positions:
000 001 002 100 101 102 200 201 202
010 011 012 110 111 112 210 211 212
020 021 022 120 121 122 220 221 222

On the first test, first pig will drink from first 9 bucktes: 000, 001, 002, 010, 011, 012, 020, 021, 022, if it is not dead, on the second test it drink from the second 9 buckets 100, 101, 102, 110, 111, 112, 120, 121, 122. Why we choose this bucktes? Because for the first group it always starts with 0 and second always starts with 1. What can be our results?

This pig dies after first test, so we can conclude, that our bucket has form 0**.
This pig dies after second test, so we can conclude, that our bucket has form 1**.
It will not die at all (lucky bastard), then our bucket has form 2**.
So, what was the purpuse of first pig? To understand the first digit in our bucket number.

No, let us look at the second pig: we do very similar procedure for it: on the first test it will drink from the 9 buckets from first line: 000, 001, 002, 100, 101, 102, 200, 201, 202: all buckets with second number equal to 0, on the second test, it will drink from 010, 011, 012, 110, 111, 112, 210, 211, 212: from all buckets with second number equel to 1. We again can do the following inference:

This pig dies after first test, so we can conclude, that our bucket has form *0*.
This pig dies after second test, so we can conclude, that our bucket has form *1*.
It will not die at all (lucky bastard), then our bucket has form *2*.
Finally, we have the third pig, which help us to understand if we have **0, **1 or **2.

Looking at all information we have now about the frist, the second and the third digits in our bucket number we can say what bucket we have!

Complexity: it is just O(1) time and space if we assume that we can evaluate log in O(1) time.

'''
class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        return ceil(log(buckets)/log(minutesToTest//minutesToDie + 1))