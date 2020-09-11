# 299. Bulls and Cows
# Easy

# 746

# 902

# Add to List

# Share
# You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

# Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

# Please note that both secret number and friend's guess may contain duplicate digits.

# Example 1:

# Input: secret = "1807", guess = "7810"

# Output: "1A3B"

# Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
# Example 2:

# Input: secret = "1123", guess = "0111"

# Output: "1A1B"

# Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
# Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

# This solution works !

from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        counts = Counter(secret)
   
        a = 0
        b = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a+=1
                counts[secret[i]]-=1
                if counts[secret[i]]<=0:
                    del counts[secret[i]]
        # print(counts)
        for i in range(len(secret)):
            # print(secret[i], guess[i])
            if secret[i] != guess[i]:
                if guess[i] in counts:
                    b+=1
                    counts[guess[i]]-=1
                    if counts[guess[i]]<=0:
                        del counts[guess[i]]
        # print(counts)
        return str(a)+"A"+str(b)+"B"
    
    
# Other solutions:
# use Counter to count guess and secret and sum their overlap. Then use zip to count A.
def getHint(self, secret, guess):
    s, g = Counter(secret), Counter(guess)
    a = sum(i == j for i, j in zip(secret, guess))
    return '%sA%sB' % (a, sum((s & g).values()) - a)

def getHint(self, secret, guess):
    bulls = sum(map(operator.eq, secret, guess))
    both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
    return '%dA%dB' % (bulls, both - bulls)


def getHint(self, secret, guess):
        A = sum(a==b for a,b in zip(secret, guess))
        B = collections.Counter(secret) & collections.Counter(guess)
        return "%dA%dB" % (A, sum(B.values()) - A)

# intuitive way !!!!

def getHint(self, secret, guess):
    slist=list(secret)
    glist=list(guess)
    i=0
    A=0
    while i <len(slist) and i<len(glist):
        if slist[i] == glist[i]:
            A+=1
            slist[i]=None
            glist[i]=None
        i+=1
    scounts = Counter(slist)
    gcounts = Counter(glist)
    
    B=0
    for k in gcounts:
        if k is not None and k in scounts:
            B+=min(scounts[k],gcounts[k])
    return '{}A{}B'.format(A,B)