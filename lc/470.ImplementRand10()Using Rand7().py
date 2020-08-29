# 470. Implement Rand10() Using Rand7()

# Given a function rand7 which generates a uniform random integer in the range 1 to 7, 
# write a function rand10 which generates a uniform random integer in the range 1 to 10.

# Do NOT use system's Math.random().


# Example 1:

# Input: 1
# Output: [7]
# Example 2:

# Input: 2
# Output: [8,4]
# Example 3:

# Input: 3
# Output: [8,1,10]


# Note:

# rand7 is predefined.
# Each testcase has one argument: n, the number of times that rand10 is called.


# Follow up:

# What is the expected value for the number of calls to rand7() function?
# Could you minimize the number of calls to rand7()?



# This solution works ! Very intuitive way:

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        
        STEP1:
        123 - 4 - 567
        
        STEP2:
        12345 - 67 5+(12345) - 67
        """
        
        # do rand7()
        # 123 -> 12345
        # 4 -> do it again
        # 567 -> 678910
        num1 = 4
        while num1 == 4:
            num1 = rand7()
            
        # do rand7() again
        # 12345 -> return as it is if the first number was 123 else 5+ the number
        # 67 -> do it again 
        num2 = 6
        while num2 == 6 or num2 == 7:
            num2 = rand7()
        if num1<4:
            return num2
        elif num1>4:
            return num2+5
    




# This solution works !

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        rand40 = 40
        while rand40 >= 40:
            rand40 = (rand7() - 1) * 7 + rand7() - 1
        return rand40 % 10 + 1
    
# Solution 0: Easy Solution with random 49
# rand7() will get random 1 ~ 7
# (rand7() - 1) * 7 + rand7() - 1 will get random 0 ~ 48
# We discard 40 ~ 48, now we have rand40 equals to random 0 ~ 39.
# We just need to return rand40 % 10 + 1 and we get random 1 ~ 10.

# In 9/49 cases, we need to start over again.
# In 40/49 cases, we call rand7() two times.

# Overall, we need 49/40*2 = 2.45 calls of rand7() per rand10().


# Intuition of Improvement:
# Solution 0 is a good answer and you may pass a interview with this solution.
# The average call of rand7 here is 2.45 calls.

# However, we may think about, what is the limit?
# Is that possible to get an average of 2 calls.


# What is the Limit
# It may seem impossible, but unfortunately, even average 2 is still far from the best answer.

# The problem is that you generate 49 random states, waste 9 of them.
# And we arrange the rest 40 states into 10 states.
# You can see that in that solution,
# 80% of random states waste and we satisfy with only 20% efficiency.

# Did a quick math for the limit log10 / log7 = 1.1833,
# which lead me to find the following solution.


# Solution 1: instead of 49, we use bigger pow of 7:
# rand10() will consume the generated random integer from stack cache.
# If cache is empty, it will call function generate().

# In generate(), it will generate an integer in range [0, 7^19].
# 7^19 = 11398895185373143, and close to an pow of 10.
# So in 11398895185373140 / 11398895185373143 = 99.99999999999997% cases, it will generate at least 1 integer.
# And in 10000000000000000 / 11398895185373143 = 87.73% cases, it will generate 16 integers.

# N = 19 is the best we can choose in long integer range,
# and N = 7 is another good choice for 32 bits integer range.

# This solution got average 1.199 calls, it's really close to theoretic limit.


    cache = []
    def rand10(self):
        while not self.cache: self.generate()
        return self.cache.pop()

    def generate(self):
        n = 19  # 1.199
        cur = sum((self.rand7() - 1) * (7**i) for i in range(n))
        rang = 7 ** n
        while cur < rang / 10 * 10:
            self.cache.append(cur % 10 + 1)
            cur /= 10
            rang /= 10
            

# Solution 2: No need to decide the pow in advance
# Someone may have a concern,
# how can we find a magic pow like 19 or 7?

# Actually, we don't need to.
# Continue to improve the solution 1,
# we cache a big random number.
# And when we need a rand10, we take a part from it.


    def rand10(self):
        cache, upper = self.cache, self.upper
        while upper < 10**9:
            cache, upper = cache * 7 + self.rand7() - 1, upper * 7
        res = cache % 10 + 1
        self.cache, self.upper = cache / 10, upper / 10
        self.count10 += 1  # test
        self.count[res] += 1  # test
        return res
    
# This solution will achieve 1.183 calls of rand7() per rand10().