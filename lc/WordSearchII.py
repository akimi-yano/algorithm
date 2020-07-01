# Word Search II
class Solution:
# TLE!!! dont use this 
    # def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         Input: 
#         board = [
#           ['o','a','a','n'],
#           ['e','t','a','e'],
#           ['i','h','k','r'],
#           ['i','f','l','v']
#         ]
#         words = ["oath","pea","eat","rain"]

#         Output: ["eat","oath"]

        # if len(board)==0 and len(board[0])==0:
        #     return []
    
        # def helper(look,i,t_row,t_col):
        #     # print(look[i:], t_row, t_col)
        #     if t_row < 0 or t_col < 0 or t_row > len(board)-1 or t_col > len(board[0])-1:
        #         return 

        #     if board[t_row][t_col] is not None and board[t_row][t_col] == look[i]:
        #         # append to ans if the word matches
        #         if i == len(look)-1:
        #             ans.add("".join(look))
        #             return 
        #         # if you use the word, delete from choices
        #         visited = board[t_row][t_col]
        #         board[t_row][t_col] = None

        #         helper(look,i+1,t_row+1,t_col)
        #         helper(look,i+1,t_row-1,t_col)
        #         helper(look,i+1,t_row,t_col+1)
        #         helper(look,i+1,t_row,t_col-1)
                
        #         board[t_row][t_col] = visited

           
        # memo = {}
        # ans = set([])
        # for word in words:
        #     if word[0] not in memo:
        #         memo[word[0]] = [word]
        #     else:
        #         memo[word[0]].append(word)
        # # print(memo)
        # for row in range(len(board)):
        #     for col in range(len(board[row])):
        #         if board[row][col] in memo:
        #             for choice in memo[board[row][col]]:
        #                 if choice in ans:
        #                     continue
        #                 helper(choice,0,row,col)
        # return ans 
        
        
        
    # this works !!!
   def findWords(self, board, words):
        
        def dfs(row, col, a_dict, word):
            
            if '*' in a_dict and a_dict['*'] == True:
                result.append(word)
                a_dict['*'] = False
                if len(a_dict) == 1:
                    return
                
            if row < 0 or row > size-1 or col < 0 or col > col_size-1:
                return
            
            if board[row][col] not in a_dict:
                return
            
            char = board[row][col]
            a_dict = a_dict[board[row][col]]
            word += char
            
            board[row][col] = '#'
            dfs(row+1, col, a_dict, word)
            dfs(row, col+1, a_dict, word)
            dfs(row-1, col, a_dict, word)
            dfs(row, col-1, a_dict, word)
            board[row][col] = char
                
            
        if not board or not words: return []
        
        size = len(board)
        col_size = len(board[0])
        result = []
        trie_root = {}
        for word in words:
            w_dict = trie_root
            for c in word:
                if c not in w_dict:
                    w_dict[c] = {}
                w_dict = w_dict[c]
            w_dict['*'] = True
        
        for i in range(size):
            for j in range(col_size):
                if board[i][j] in trie_root:
                    dfs(i,j,trie_root,'')
                
        return result
                
s= Solution()
print(s.findWords([
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
],["oath",'ocean',"pea","eat","rain"]))       

# words = ["oath",'ocean',"pea","eat","rain"]

#   {'o': 
#        {'a': 
#             {'t': 
#                  {'h': 
#                       {'#': True}}}, 
#         'c': 
#             {'e': 
#                  {'a': 
#                       {'n': {'#': True}}}}}, 
#     'p': 
#         {'e': 
#              {'a': 
#                   {'#': True}}}, 
#     'e': 
#         {'a': 
#              {'t': 
#                   {'#': True}}}, 
#     'r': 
#         {'a':
#              {'i': 
#                   {'n': 
#                        {'#': True}}}}}
    
    # Time O(MN * 4^K) Space O(M), K = length of word, M = no.of letters in Trie, time = 284 ms
    
    
    
    
    
    
    
    
    
    

# fixed my code and I did it again and it works !!! so proud !!! 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(board)==0 and len(board[0])==0:
            return []
    
        ans = []
        def helper(t_row, t_col, substr, node):
            # print(look[i:], t_row, t_col)
            if t_row < 0 or t_col < 0 or t_row > len(board)-1 or t_col > len(board[0])-1:
                return

            if board[t_row][t_col] is not None and board[t_row][t_col] in node:
                char = board[t_row][t_col]
                substr += char
                board[t_row][t_col] = None
                next_node = node[char]
                if '#' in next_node and next_node['#']:
                    ans.append(substr)
                    next_node['#'] = False
                helper(t_row+1,t_col, substr, next_node)
                helper(t_row-1,t_col, substr, next_node)
                helper(t_row,t_col+1, substr, next_node)
                helper(t_row,t_col-1, substr, next_node)
                board[t_row][t_col] = char

        memo = {}
        for word in words:
            trie_node = memo
            for i in range(len(word)):
                if word[i] not in trie_node:
                    trie_node[word[i]] = {}
                trie_node = trie_node[word[i]]
            trie_node['#'] = True

        # print(memo)

        for row in range(len(board)):
            for col in range(len(board[row])):
                helper(row, col, "", memo)
        return ans 
     