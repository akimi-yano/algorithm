# H-Index
# Given an array of citations (each citation is a non-negative integer) of a researcher, 
# write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her 
# N papers have at least h citations each, and the other N − h papers have no more than h citations each."

# Example:

# Input: citations = [3,0,6,1,5]
# Output: 3 
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
#              received 3, 0, 6, 1, 5 citations respectively. 
#              Since the researcher has 3 papers with at least 3 citations each and the remaining 
#              two with no more than 3 citations each, her h-index is 3.
# Note: If there are several possible values for h, the maximum one is taken as the h-index.


#     [3,0,6,1,5]
# more than or equal to 3: 3,5,6
# less than 3: 0,1

# [0,1,3,5,6]

#     [3,0,6,1,5] 
# 5    
# 4
# 3
# 2
# 1
# 0

# [0] -> 0


# this does not work 

    # def hIndex(self, citations: List[int]) -> int:
    #     if not citations:
    #         return 0

    #     citations.sort(reverse=True)
    #     # print(citations)
    #     for i, val in enumerate(citations):
    #         # print(max_length-1-i+1,val)
    #         if val<=i+1:
    #             return min(i+1,val)
    #     return min(1,citations[0])
    
    
    
# this  works!

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort( reverse = True )
        
        for idx, citation in enumerate(citations):

            # find the first index where citation is smaller than or equal to array index            
            if idx >= citation:
                return idx
        
        return len(citations)
    

# this works ! super straight forward


def hIndex(citations):
    return sum(i < val for i, val in enumerate(sorted(citations, reverse=True)))

print(hIndex([0,1,3,5,6]))
print(hIndex([0]))

# [6,5,3,1,0]
# [1,1,1,0,0]=3

# you reverse sort the  array and compare the index  with its value 
# if the index is smaller  than  val, 1
# else its  0
# add all 1s and  return 

'''
bucket sort solution O(N) !
if you know the range of value: 0-N

public int hIndex(int[] citations) {
    int n = citations.length;
    int[] buckets = new int[n+1];
    for(int c : citations) {
        if(c >= n) {
            buckets[n]++;
        } else {
            buckets[c]++;
        }
    }
    int count = 0;
    for(int i = n; i >= 0; i--) {
        count += buckets[i];
        if(count >= i) {
            return i;
        }
    }
    return 0;
}

'''