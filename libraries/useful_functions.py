# USEFUL FUNCTIONS:

# .index() - return the first index of character or substring
# .rindex() -  return the first index of character or substring


str1 = "this is string example....wow!!!"
str2 = "is"
str3 = "z"

print(str1.rindex(str2))
print(str1.index(str2))

try:
    print(str1.rindex(str3))
    print(str1.index(str3))
except:
    print(-1)
    print(-1)
    
    
test = "I wanna see how: this sentence will be splitted."

print(test.split()) # space are gone
print(test.split(":"))  # : is gone but the space stays and its not splitted by space

