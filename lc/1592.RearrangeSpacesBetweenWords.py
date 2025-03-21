# 1592. Rearrange Spaces Between Words
# Easy

# 7

# 7

# Add to List

# Share
# You are given a string text of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that text contains at least one word.

# Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the returned string should be the same length as text.

# Return the string after rearranging the spaces.



# Example 1:

# Input: text = "  this   is  a sentence "
# Output: "this   is   a   sentence"
# Explanation: There are a total of 9 spaces and 4 words. We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.
# Example 2:

# Input: text = " practice   makes   perfect"
# Output: "practice   makes   perfect "
# Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces plus 1 extra space. We place this extra space at the end of the string.
# Example 3:

# Input: text = "hello   world"
# Output: "hello   world"
# Example 4:

# Input: text = "  walks  udp package   into  bar a"
# Output: "walks  udp  package  into  bar  a "
# Example 5:

# Input: text = "a"
# Output: "a"


# Constraints:

# 1 <= text.length <= 100
# text consists of lowercase English letters and ' '.
# text contains at least one word.


# This solution  works  !!!

class Solution:
    def reorderSpaces(self, text: str) -> str:
        word_count = 0
        space_count = 0
        for c in text:
            if c == " ":
                space_count+=1
        text_list = text.split()
        if len(text_list) < 2:
            return "".join(text_list) + " " * space_count
        word_count = len(text_list)
        # print(space_count, word_count)
        
        if space_count % (word_count-1) == 0:
            each_space = space_count // (word_count-1)
            end = 0
        else:
            each_space = space_count // (word_count-1)
            end = space_count % (word_count-1) 
            
        ans = ""
        for i in range(len(text_list)):
            ans += text_list[i]
            if i != len(text_list)-1:
                ans += " " * each_space
            else:
                ans += " " * end
        return ans
    

# code after a code review !:

class Solution:
    def reorderSpaces(self, text: str) -> str:
        word_count = 0
        space_count = 0
        for c in text:
            if c == " ":
                space_count+=1
        text_list = text.split()
        if len(text_list) < 2:
            return "".join(text_list) + " " * space_count
        word_count = len(text_list)

        each_space = space_count // (word_count-1)
        end = space_count % (word_count-1) 
            
        ans = ""
        for i in range(len(text_list)-1):
            ans += text_list[i] + " " * each_space
        ans += text_list[-1] + " " * end
        return ans