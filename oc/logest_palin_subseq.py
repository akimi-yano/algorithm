s = "ABCADDCBA"
def longest_palindrom(s):
  cache = {}
  def traverse(start, end):
    if start > end:
      return 0 
    if start == end:
      return 1
    if s[start] == s[end]:
      return 2+ traverse(start+1, end-1)
    
    else:
      # cache[(start,end)] = 
      return max(traverse(start+1, end), traverse(start,end-1))
    
   
  return traverse(0, len(s)-1)
        
print(longest_palindrom(s))