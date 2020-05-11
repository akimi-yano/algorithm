def reverseVowels(word):
    # Write your code here
    vowls = set(["a","i","u","e","o","A","I","U","E","O"])
    temp = []
    ans = ""
    for c in word:
        if c in vowls:
            temp.append(c)
    for s in word:
        if s in vowls:
            ans+=temp.pop()
        else:
            ans+=s
    word = ans
    return word
print(reverseVowels("san francisco"))

