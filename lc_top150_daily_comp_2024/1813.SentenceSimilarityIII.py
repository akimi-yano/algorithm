'''
1813. Sentence Similarity III
Solved
Medium
Topics
Companies
Hint
You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.

Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. Note that the inserted sentence must be separated from existing words by spaces.

For example,

s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in s1.
s1 = "Frog cool" and s2 = "Frogs are cool" are not similar, since although there is a sentence "s are" inserted into s1, it is not separated from "Frog" by a space.
Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.

 

Example 1:

Input: sentence1 = "My name is Haley", sentence2 = "My Haley"

Output: true

Explanation:

sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".

Example 2:

Input: sentence1 = "of", sentence2 = "A lot of words"

Output: false

Explanation:

No single sentence can be inserted inside one of the sentences to make it equal to the other.

Example 3:

Input: sentence1 = "Eating right now", sentence2 = "Eating"

Output: true

Explanation:

sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.

 

Constraints:

1 <= sentence1.length, sentence2.length <= 100
sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
The words in sentence1 and sentence2 are separated by a single space.
'''

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        w1 = sentence1.split(' ')
        w2 = sentence2.split(' ')
        if len(w1) > len(w2):
            w1, w2 = w2, w1
        # if w1 matches the prefix or suffix of w2
        if w1 == w2[:len(w1)] or w1 == w2[-len(w1):]:
            return True
        #else, we must split w1
        for i in range(1, len(w1)):
            first = w1[:i]
            second = w1[i:]
            # print(first, second, w2[:len(first)], w2[-len(second):])
            if first == w2[:len(first)] and second == w2[-len(second):]:
                return True
        return False

# Slight optimization of code:

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        w1 = sentence1.split(' ')
        w2 = sentence2.split(' ')
        if len(w1) > len(w2):
            w1, w2 = w2, w1

        for i in range(0, len(w1)+1):
            first = w1[:i]
            second = w1[i:]
            w2_first = w2[:len(first)]
            w2_second = w2[-len(second):] if len(second) else []
            # print(first, w2_first, second, w2_second)
            if first == w2_first and second == w2_second:
                return True
        return False