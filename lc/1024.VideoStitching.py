# 1024. Video Stitching
# Medium

# 580

# 28

# Add to List

# Share
# You are given a series of video clips from a sporting event that lasted T seconds.  These video clips can be overlapping with each other and have varied lengths.

# Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends at time clips[i][1].  We can cut these clips into segments freely: for example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].

# Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event ([0, T]).  If the task is impossible, return -1.


# Example 1:

# Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
# Output: 3
# Explanation: 
# We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
# Then, we can reconstruct the sporting event as follows:
# We cut [1,9] into segments [1,2] + [2,8] + [8,9].
# Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].
# Example 2:

# Input: clips = [[0,1],[1,2]], T = 5
# Output: -1
# Explanation: 
# We can't cover [0,5] with only [0,1] and [1,2].
# Example 3:

# Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
# Output: 3
# Explanation: 
# We can take clips [0,4], [4,7], and [6,9].
# Example 4:

# Input: clips = [[0,4],[2,8]], T = 5
# Output: 2
# Explanation: 
# Notice you can have extra video after the event ends.


# Constraints:

# 1 <= clips.length <= 100
# 0 <= clips[i][0] <= clips[i][1] <= 100
# 0 <= T <= 100


# This approach does not work : 


# class Solution:
#     def videoStitching(self, clips: List[List[int]], T: int) -> int:
#         clips.sort(key = lambda x: (x[0],-x[1]))
#         start_min = float('inf')
#         end_max = float('-inf')
#         count = 0
#         # print(clips)
#         for start, end in clips:
#             if start < start_min or end > end_max:
#                 count += 1
#                 # print((start, end))
#                 start_min = min(start_min, start)
#                 end_max = max(end_max, end)
        
#         if start_min !=0 or end_max!= T:
#             return -1
#         else:
#             return count
#         '''
#         inclusive
#         [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
#         0 1 2 3 4 5 6 7 8 9 10
#         - - - O
#                 - - - 
#                         - -  - O
#           - - - - - - - - -  O 
#           - - - - -
#                   - - - - -  
#         '''



# This approach does not work:

# class Solution:
#     def videoStitching(self, clips: List[List[int]], T: int) -> int:

#         def helper(i, covered):
#             if i > len(clips) -1:
#                 return float('inf')
#             if covered >= T:
#                 return 0
#             start, end = clips[i]
#             min_num_intervals = float('inf')
#             min_num_intervals = min(min_num_intervals, 1+helper(i+1, end))
#             min_num_intervals = min(min_num_intervals, helper(i+1, covered))
#             return min_num_intervals
        
#         clips.sort(key = lambda x: (x[0],-x[1]))
#         start, end = clips[0]
#         if start >0:
#             return -1
        
#         return helper(0, 0)
        
        
        
# This solution works !
'''
greedy algorithm ! 
sort by the start
if needed < start then we do ans +=1
if needed >= T:
    return ans
if needed < start after the operation -> return -1
keep updating best end and needed

'''
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        if T < 1:
            return 0
        clips.sort()

        ans = 0
        # needed = the point that needs to be covered
        needed = 0
        # best_end = the next best end
        best_end = float('-inf')
        for start, end in clips:
            # if needed becomes smaller than the current interval's start
            if needed < start:
                ans += 1
                needed = best_end
                # if needed is >= T, we are done. Return ans.
                if needed >= T:
                    return ans
            # if needed is still smaller than the current interval's start, it's
            # not possible to connect the intervals. Return -1.
            if needed < start:
                return -1
            # update best_end to the max between best_end the current interval's end.
            best_end = max(best_end, end)
            # if best_end is >= T, we are done. Return ans + 1 (because the current
            # inteval is not added to ans yet).
            if best_end >= T:
                return ans + 1
        # if we looped through everything without returning, it was impossible. Return -1.
        return -1