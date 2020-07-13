# 744. Find Smallest Letter Greater Than Target

# Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

# Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

# Examples:
# Input:
# letters = ["c", "f", "j"]
# target = "a"
# Output: "c"

# Input:
# letters = ["c", "f", "j"]
# target = "c"
# Output: "f"

# Input:
# letters = ["c", "f", "j"]
# target = "d"
# Output: "f"

# Input:
# letters = ["c", "f", "j"]
# target = "g"
# Output: "j"

# Input:
# letters = ["c", "f", "j"]
# target = "j"
# Output: "c"

# Input:
# letters = ["c", "f", "j"]
# target = "k"
# Output: "c"
# Note:
# letters has a length in range [2, 10000].
# letters consists of lowercase letters, and contains at least 2 unique letters.
# target is a lowercase letter.


class Solution:
    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    #     target_n = ord(target)-ord('a')
    #     for ch in letters:
    #         if ord(ch)-ord('a')>target_n:
    #             return ch
    #     return letters[0]
    
    
    # def nextGreatestLetter(self, letters, target):
    #     for letter in letters:
    #         if letter > target:
    #             return letter
    #     return letters[0] # If not found

    
# # Using bisect:
    def nextGreatestLetter(self, letters, target):
        # bisect.bisect_right(letters, target) finds the index position
        # where you should insert the same elem (on the right side)
        # if its not found, returns the len(letters)
        
        pos = bisect.bisect_right(letters, target)
        return letters[0] if pos == len(letters) else letters[pos]
    

        # bisect.bisect_left returns the leftmost place in the sorted list to insert the given element. 
        # bisect.bisect_right returns the rightmost place in the sorted list to insert the given element.

        # An alternative question is when are they equivalent? By answering this, the answer to your question becomes clear.

        # They are equivalent when the the element to be inserted is not present in the list. 
        # Hence, they are not equivalent when the element to be inserted is in the list.