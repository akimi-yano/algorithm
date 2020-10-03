# 1604. Alert Using Same Key-Card Three or More Times in a One Hour Period
# Medium

# 20

# 47

# Add to List

# Share
# Leetcode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.

# You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and the time when their key-card was used in a single day.

# Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".

# Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.

# Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "23:51" - "00:10" is not considered to be within a one-hour period.

 

# Example 1:

# Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
# Output: ["daniel"]
# Explanation: "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").
# Example 2:

# Input: keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
# Output: ["bob"]
# Explanation: "bob" used the keycard 3 times in a one-hour period ("21:00","21:20", "21:30").
# Example 3:

# Input: keyName = ["john","john","john"], keyTime = ["23:58","23:59","00:01"]
# Output: []
# Example 4:

# Input: keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"], keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]
# Output: ["clare","leslie"]
 

# Constraints:

# 1 <= keyName.length, keyTime.length <= 105
# keyName.length == keyTime.length
# keyTime are in the format "HH:MM".
# [keyName[i], keyTime[i]] is unique.
# 1 <= keyName[i].length <= 10
# keyName[i] contains only lowercase English letters.



# This solution does not work !!!
# class Solution:
#     def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
#         adj_list = {}
#         for i in range(len(keyName)):
#             if keyName[i] not in adj_list:
#                 adj_list[keyName[i]] = []
#             adj_list[keyName[i]].append(keyTime[i].split(":"))
        
#         ans = []
        
#         for name, times in adj_list.items():
#             prev_h = float('-inf')
#             prev_m = float('-inf')
#             count = 1

                # cur_h, cur_m = int(time[0]), int(time[1])
                # print(cur_h, prev_h , cur_m, prev_m, cur_h - prev_h, count)
                # if cur_h - prev_h > 1 or (cur_h - prev_h == 1 and cur_m > prev_m) :
                #     prev_h = cur_h
                #     prev_m = cur_m
                #     count -= 1
                #     if count == 0:
                #         count = 1
                # else:
                #     print('here')
                #     count += 1
                #     if count >= 3:
                #         ans.append(name)
                #         # print(name, count)
        #         #         break
        # ans = list(set(ans))
        # return sorted(ans)
            
            
            
            

# This solution works !!!! used queue popleft
# dont forget to sort 
# don't call it adj_list if its not graph

from collections import deque
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        memo = {}
        for i in range(len(keyName)):
            if keyName[i] not in memo:
                memo[keyName[i]] = []
            memo[keyName[i]].append(keyTime[i].split(":"))
        
        ans = []
        
        for name, times in memo.items():
            queue = deque([])
            for time in sorted(times):
                cur_h, cur_m = int(time[0]), int(time[1])
                queue.append((cur_h, cur_m))
                while queue[-1][0] - queue[0][0] > 1 or (queue[-1][0] - queue[0][0] == 1 and queue[-1][1] > queue[0][1]):
                    queue.popleft()
                if len(queue) >= 3:
                    ans.append(name)
        ans = list(set(ans))
        return sorted(ans)
