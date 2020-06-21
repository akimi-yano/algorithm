# 275. H - index II
# Given an array of citations sorted in ascending order (each citation is a non-negative integer) 
# of a researcher, write a function to compute the researcher's h-index.
# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N 
# papers have at least h citations each, and the other N − h papers have no more than h citations each."

def hIndex(citations):
    N = len(citations)
    head = 0
    tail = N
    
    while head < tail:
        mid = (head+ tail)//2
        numBigger = N - mid
        
        if numBigger <= citations[mid]:
            tail = mid 
        else:
            head = mid + 1
    # at the end, head is  the index I want   
    return N - head
    
print(hIndex([0,1,3,5,6]))  # return 3 
print(hIndex([1,4,4,4,5])) # return 4 - there are 4 numbers whose value is larger or equal to 4

# numBigger gets bigger as  the mid shifts to right until you get to the index that is not meeitng the requirement.
# and then you move to the right once and return the   N- head



# JUST FYI but this one is less intuitive.
# I think the one above is easier to understand.

# The basic idea of this solution is to use binary search to find the minimum index such that

# citations[index] >= length(citations) - index
# After finding this index, the answer is length(citations) - index.

# This logic is very similar to the C++ function lower_bound or upper_bound.
    def hIndex(self, citations: List[int]) -> int:
           
        length = len(citations)
        
        first = 0
        count = length
        
        while count > 0:
            step = count // 2
            mid = first + step
            if citations[mid] < length - mid:
                first = mid + 1
                count -= (step + 1)
            else:
                count = step
        
        return length - first