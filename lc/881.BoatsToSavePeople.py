# 881. Boats to Save People
# Medium

# 1050

# 46

# Add to List

# Share
# The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

# Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

 

# Example 1:

# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# Example 2:

# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# Example 3:

# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
# Note:

# 1 <= people.length <= 50000
# 1 <= people[i] <= limit <= 30000


# This solution works

from collections import Counter
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        total = 0
        members = Counter(people)
        for person in people:
            if person not in members:
                continue
            remainingmax = limit - person
            for the_other in range(remainingmax, 0, -1):
                if the_other in members:
                    if the_other == person:
                        if members[person] > 1:
                            members[person] -= 2
                            if members[person] < 1:
                                del members[person]
                            total += 1
                            break
                    else:
                        members[the_other] -= 1
                        if members[the_other] < 1:
                            del members[the_other]
                        members[person] -= 1
                        if members[person] < 1:
                            del members[person]
                        total += 1
                        break
        for v in members.values():
            total += v
        return total
    
# This solution works - optimization

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse = True)
        total = 0
        fat, skinny = 0, len(people)-1
        while fat <= skinny:
            if people[fat] + people[skinny] <= limit:
                skinny -=1
            fat += 1
            total +=1
        return total