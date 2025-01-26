'''
2127. Maximum Employees to Be Invited to a Meeting
Hard
Topics
Companies
Hint
A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.

The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.

Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.

 

Example 1:


Input: favorite = [2,2,1,2]
Output: 3
Explanation:
The above figure shows how the company can invite employees 0, 1, and 2, and seat them at the round table.
All employees cannot be invited because employee 2 cannot sit beside employees 0, 1, and 3, simultaneously.
Note that the company can also invite employees 1, 2, and 3, and give them their desired seats.
The maximum number of employees that can be invited to the meeting is 3. 
Example 2:

Input: favorite = [1,2,0]
Output: 3
Explanation: 
Each employee is the favorite person of at least one other employee, and the only way the company can invite them is if they invite every employee.
The seating arrangement will be the same as that in the figure given in example 1:
- Employee 0 will sit between employees 2 and 1.
- Employee 1 will sit between employees 0 and 2.
- Employee 2 will sit between employees 1 and 0.
The maximum number of employees that can be invited to the meeting is 3.
Example 3:


Input: favorite = [3,0,1,4,1]
Output: 4
Explanation:
The above figure shows how the company will invite employees 0, 1, 3, and 4, and seat them at the round table.
Employee 2 cannot be invited because the two spots next to their favorite employee 1 are taken.
So the company leaves them out of the meeting.
The maximum number of employees that can be invited to the meeting is 4.
 

Constraints:

n == favorite.length
2 <= n <= 105
0 <= favorite[i] <= n - 1
favorite[i] != i
'''

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        '''
        Choose the larger one of these 2 cases:
        - The maximum circle in this graph.
        - The sum of all the longest chain containing all the pairs.
        '''
        # find largest circles
        N = len(favorite)
        max_circle = 0
        seen = [0] * N
        for i in range(N):
            # if the person has not been visited
            if seen[i] == 0:
                # start_person is for locating the first visited person
                start_person = i
                # cur_person is for the current person we are visiting
                cur_person = i
                # cur_set to store all the visited persons in this iteration
                cur_set = set()

                # as long as we are visiting new person, we keep finding the person's fav person
                while seen[cur_person] == 0:
                    seen[cur_person] = 1
                    cur_set.add(cur_person)
                    cur_person = favorite[cur_person]
                
                # until we find the first visited person
                # depends on if this visited person has been visited in earlier iteration or 
                # just this iteration
                if cur_person in cur_set: # if current person is in current set, meaning we foudn a new circle
                    cur_sum = len(cur_set)

                    # use the start_person to find the distance from the first visited person in this iteration
                    # to this current person
                    while start_person != cur_person:
                        cur_sum -= 1
                        start_person = favorite[start_person]
                    max_circle = max(max_circle, cur_sum)

        # find the sum of largest arms.
        # first, find all mutually favorite persons
        pair = []
        visited = [0] * N
        for idx in range(N):
            # if a is b s favorite person vise versa, put them in the pair list
            if favorite[favorite[idx]] == idx and visited[idx] == 0:
                pair.append([idx, favorite[idx]])
                visited[idx] = 1
                visited[favorite[idx]] = 1
            
        # for every person I, find out all the persons whose favorite is I
        res = 0
        child = collections.defaultdict(list)
        for i in range(N):
            child[favorite[i]].append(i)

        for a, b in pair:
            # max arm length start from first person a
            maxa = 0
            dq = collections.deque()
            for cand in child[a]:
                if cand != b:
                    dq.append([cand, 1])
            while dq:
                cur, n = dq.popleft()
                maxa = max(maxa, n)
                for nxt in child[cur]:
                    dq.append([nxt, n+1])
            
            # max arm length start from first people b
            maxb = 0
            dq = collections.deque()
            for cand in child[b]:
                if cand != a:
                    dq.append([cand, 1])
            while dq:
                cur, n = dq.popleft()
                maxb = max(maxb, n)
                for nxt in child[cur]:
                    dq.append([nxt, n+1])
            # the total length is the 2 longest arm plus 2 (a and b themselves)
            res += 2 + maxa + maxb
        # choose the larger one as the anser
        return max(max_circle, res)