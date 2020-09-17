'''269. Alien Dictionary
Hard

1916

380

Add to List

Share
There is a new alien language which uses the latin alphabet. However, the order 

among letters are unknown to you. You receive a list of non-empty words from the dictionary, 
where words are sorted lexicographically by the rules of this new language. Derive the order of
letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.

'''

class Solution:
    
    def alienOrder(self, words: List[str]) -> str:
        
        
        def create_graph():
        
            chars = set(''.join(words))
            g_dict = {char: [] for char in chars}
            reverse_dict = {char: [] for char in chars}

            for i in range(len(words)-1):
                w1 = words[i]
                w2 = words[i+1]
                
                if len(w1) > len(w2) and w1[:len(w2)] == w2:
                    return {}, {}  
                for j in range(min(len(w2), len(w1))):
                    char1 = w1[j]
                    char2 = w2[j]
                    if char1 != char2:
                        if char2 not in g_dict[char1]:
                            g_dict[char1].append(char2)
                            # print(f'create graph {g_dict}')
                            reverse_dict[char2].append(char1)
                        break
                            
            return g_dict, reverse_dict
                
        
        def topological_sort(g_dict, reverse_dict):
            
            todo = collections.deque([k for k,v in reverse_dict.items() if not v])
            result = ''
            
            # a->b z->c
            while todo:
                # print(todo)
                node = todo.popleft()
                result += str(node)
                
                for next_node in g_dict[node]:
                    # print(f'{node} {next_node}')
                    reverse_dict[next_node].remove(node)
                    if not reverse_dict[next_node]:
                        # print('here')
                        todo.append(next_node)
                        # print(todo)
                        
                # print(reverse_dict)
                # print(f'result = {result}')
                            
            if len(result) < len(reverse_dict):
                return ''
            
            return result
        
        
        if not words: return ''
        g_dict, reverse_dict = create_graph()
        # print(g_dict)
        if g_dict == {}:
            return ''
        return topological_sort(g_dict, reverse_dict)