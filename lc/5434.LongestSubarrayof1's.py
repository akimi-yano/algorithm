# 5434. Longest Subarray of 1's After Deleting One Element


        # you must remove one elem (0 or 1)
        # return the number of continuous 1's
        # sliding window 
        # [0,1,1,1,0,1,1,0,1]
         #         l       r       
        # count 6
        # removed = True
        
        # 1set left and right at the beginning of arr
        # 2move right until they see 0 and removed == true
        # 3    while if they see 0 and removed == true, start moving left idx and until left sees next 0 removed 
        # 2include the count for the right 0 and move forward the right until sees 0 and removed == true
    
        
# this doesnt work ! look below for a solution that works
        
# class Solution:
    # def longestSubarray(self, nums: List[int]) -> int:
        
        # max_count = 0
        # count = 0
        # removed = False
        # left = 0
        # right = 1
        
        # if nums[left] == 0 and removed == False:
        #     removed = True
        # count+=1 
        
        # while left<len(nums):
        #     if nums[right] == 1:
        #         count+=1
        #         right+=1
        #         max_count = max(max_count,count) 
            
        #     elif nums[right] == 0 and removed == True:    
        #         while removed == True and left<len(nums):
        #             if nums[left]==1:
        #                 left+=1
        #                 count-=1
        #             else:
        #                 removed = False
        #                 count+=1
        #             max_count = max(max_count,count)    
        # return max_count
                
            
            
            
            
            
# This one works !        
            
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        if sum(nums) == len(nums):
            return len(nums) - 1
        
        one_seqs = {}
        processing_ones = False
        cur_start = -1
        for i, elem in enumerate(nums):
            if elem == 1:
                if not processing_ones:
                    processing_ones = True
                    cur_start = i
            else:
                if processing_ones:
                    processing_ones = False
                    cur_end = i-1
                    one_seqs[cur_start] = cur_end
        if processing_ones:
            cur_end = len(nums)-1
            one_seqs[cur_start] = cur_end
        # print(one_seqs)
        
        best = 0
        for start, end in one_seqs.items():
            best = max(best, end-start+1)
            next_start = end+2 # skip over the zero immediately after end
            if next_start in one_seqs:
                next_end = one_seqs[next_start]
                best = max(best, next_end-start)
        return best