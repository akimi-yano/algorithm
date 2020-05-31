
# # Remove the minimum number of invalid parentheses in order
# #  to make the input string valid. Return all possible results.

# # Note: The input string may contain letters other than the parentheses ( and ).

# # Example 1:

# # Input: "()())()"
# # Output: ["()()()", "(())()"]
# # Example 2:

# # Input: "(a)())()"
# # Output: ["(a)()()", "(a())()"]
# # Example 3:

# # Input: ")("
# # Output: [""]

def invalid_pare(s):
    opens=close = 0
  
    if len(s) < 2:
        return [s]
  
    for paren in s:
        if paren == '(':
            opens += 1
        elif paren == ')' and opens > 0:
            opens -=1 
        elif paren == ')' and opens == 0:
            close += 1
    visted = set()
  
#   (())
    result = []
    def DFS(s, index, opens, close):
        visted.add(s)
    
        # base case
        if opens == 0 and close == 0:
            if isValid(s):
                result.append(s)
        
        for i in range(index, len(s)):
        #if char is other than "(", ")", skip
            if s[i] != "(" and s[i] != ")":
                continue
        
            # dont remove if opens / close equals 0
            if s[i] == '(' and opens == 0:
                continue
        
            if s[i] == ')' and close == 0:
                continue
      
            # otherwise remove char at i and combine char before char(arr[i]) and after char(arr[i])
            nxt = s[:i] + s[i+1:]
            if nxt not in visted:
                DFS(nxt, i, opens-(s[i] =="("), close-(s[i] == ")"))
    
    def isValid(s):
        pass
    
    DFS(s, 0, opens, close)    
print(invalid_pare("()())()"))















