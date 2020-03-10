def anagram(s):
    # base case: if s is one character or less, return it as a list with one element
    if len(s) <= 1:
        return [s]
    
    anagrams = []
    for i in range(len(s)):
        # pull out the character we chose for the first position
        first_char = s[i]
        # make a sub-string that has the chosen character removed
        sub_s = str(s[:i] + s[i + 1:])
        sub_anagram = anagram(sub_s)
        for k in range(len(sub_anagram)):
            anagrams.append(sub_anagram[k]+first_char)
    return anagrams

print(anagram("abcd"))
print(len(anagram("abcd")))