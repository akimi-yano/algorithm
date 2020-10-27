'''
LRU Cache
https://leetcode.com/problems/lru-cache/
'''

class ListNode():
    
    def __init__(self, key, value, pre=None, next=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next


class LRUCache:
    
    def __init__(self, capacity: int):
        self.head = ListNode(None,None)
        self.tail = ListNode(None,None)
        self.capacity = capacity
        self.cache_dict = {}
        self.head.next = self.tail
        self.tail.pre = self.head
        
    def remove_node(self,node):
        
       #  1 -   2 ------3    ---4    
       # pre_n node    next_n
    
    
        pre_n = node.pre
        next_n = node.next
    
        #ponters
        pre_n.next = next_n
        next_n.pre = pre_n
      
            
            
        
        

    def move_to_head(self, node):
        
        self.remove_node(node)
        self.add_node_to_head(node)
        
        
        
    def remove_from_tail(self):
        
#         1 2 3           4         tail
#             pre_n       node
            
        # give a name
        node = self.tail.pre
        pre_n = node.pre
        
        #point
        pre_n.next = self.tail
        self.tail.pre = pre_n
        
        # return node
        
        
            
        
        
        
        
        
    def add_node_to_head(self, node):
        
#         head <--------------------> 1 <---> 2 <---> 3 <----> tail
        
#                     node           next_n
        
        
        next_n = self.head.next
        
        self.head.next = node
        node.pre = self.head
        node.next = next_n
        next_n.pre = node
        
        
    def get_size(self):
        return len(self.cache_dict)

    def get(self, key: int) -> int:
        
        #if not in the cache, return -1
        if key not in self.cache_dict:
            return -1
        
        #if in the cache, return value, move node to the head
        node = self.cache_dict[key]
        self.move_to_head(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        
        #if key doesn't exist, add item to the head
        if key not in self.cache_dict:
            node = ListNode(key,value)
            self.cache_dict[key] = node
            self.add_node_to_head(node)
            
        
        #if key exists, update the value, and move to head
        else:
            node = self.cache_dict[key]
            node.value = value
            self.move_to_head(node)
        
        #if over capacity, remove node from the tail
        #remove cache
        if self.get_size()> self.capacity:
            
            del self.cache_dict[self.tail.pre.key]
            self.remove_from_tail()
            # del self.cache_dict[tail_node.key]
            
    def p():
        
        print(self.cache_dict.keys())
        node = self.head
        while node:
            print(f'key = {node.key} value = {node.value}')
            node = node.next
        print('-------------------------------')
        
        
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
'''

'''

# Solution II: use 2 dictionary
#   
#     frequency N
#    
#         head <---> Node <---> Node <---> Node <---> tail
#                     |          |           |
#                    key 1      key 2      key 3
#                  value 1     value 2    value 3
#                   fre N       fre N       fre N
#                    
#     frequency N-1
#        ...


#     frequency 1
    
# Time O(1), Space O(), runtime = 320 ms
class ListNode():
    
    def __init__(self, key, value, fre=None, pre=None, next=None):
        self.key = key
        self.value = value
        self.fre = fre
        self.pre = pre
        self.next = next
        
        
class DLinkedList():
    
    def __init__(self):    
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.pre = self.head
        
    def remove_node(self, node):
        pre_n = node.pre
        next_n = node.next
        
        pre_n.next = next_n
        next_n.pre = pre_n
        
    def add_to_head(self, node):
        next_n = self.head.next
        
        self.head.next = node
        node.pre = self.head
        node.next = next_n
        next_n.pre = node
        
    def remove_from_tail(self):
        node = self.tail.pre
        pre_n = node.pre
        
        pre_n.next = self.tail
        self.tail.pre = pre_n
        
        return node
        

class LFUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node = {}
        self.fre_dll = {}
        self.size = 0
        self.min_fre = 1
        
    def remove(self, dll, fre):
        if dll.head.next == dll.tail:
            if self.min_fre == fre:
                self.min_fre = fre + 1
            if fre != 1:
                del self.fre_dll[fre]
        else:
            self.fre_dll[fre] = dll
        
    def remove_from_dll(self, node):
        fre = node.fre
        dll = self.fre_dll[fre]
        dll.remove_node(node)
        
        self.remove(dll, fre)
            
    def remove_from_dll_tail(self, dll, fre):
        dll.remove_from_tail()
        
        self.remove(dll, fre)
         
    def add_to_dll(self, node):
        fre = node.fre
        dll = self.fre_dll.get(fre, DLinkedList())
        dll.add_to_head(node)
        self.fre_dll[fre] = dll
     

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        
        node = self.key_node[key]
        self.remove_from_dll(node) 
        
        node.fre += node.fre
        self.add_to_dll(node)
        
        return node.value
    

    def put(self, key: int, value: int) -> None:
        if key in self.key_node:
            node = self.key_node[key]
            node.value = value

            self.remove_from_dll(node)
        
            node.fre += 1
            self.add_to_dll(node)
             
        else:
            fre = 1
            node = ListNode(key, value, fre)
            self.key_node[key] = node
            
            self.add_to_dll(node)
            
            self.size += 1
            if self.size > self.capacity:
                min_dll = self.fre_dll[self.min_fre]
            
                last_node = min_dll.tail.pre
                self.remove_from_dll_tail(min_dll,self.min_fre)
            
                del self.key_node[last_node.key]
                self.size -= 1
                
            self.min_fre = 1