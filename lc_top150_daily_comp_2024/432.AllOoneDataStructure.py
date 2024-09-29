'''
432. All O`one Data Structure
Attempted
Hard
Topics
Companies
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.

 

Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"
 

Constraints:

1 <= key.length <= 10
key consists of lowercase English letters.
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.
'''

class DLLNode:
    def __init__(self, count):
        self.count = count
        self.keys = set([])
        self.next = None
        self.prev = None

class AllOne:
    def __init__(self):
        self.key_node = {}
        self.head = DLLNode(-inf)
        self.tail = DLLNode(inf)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert_node(self, prev_node, next_node, middle_node):
        prev_node.next = middle_node
        next_node.prev = middle_node
        middle_node.prev = prev_node
        middle_node.next = next_node

    def delete_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def inc(self, key: str) -> None:
        count = None
        if key not in self.key_node:
            cur_node = self.head
            count = 1
        else:
            cur_node = self.key_node[key]
            count = cur_node.count + 1
            cur_node.keys.remove(key)

        next_node = None
        if cur_node.next.count > count:
            next_node = DLLNode(count)
            self.insert_node(cur_node, cur_node.next, next_node)
        else:
            next_node = cur_node.next
        next_node.keys.add(key)
        self.key_node[key] = next_node

        if cur_node is not self.head and len(cur_node.keys) == 0:
            self.delete_node(cur_node)
       
        # self.print_list()

    def dec(self, key: str) -> None:
        cur_node = self.key_node[key]
        cur_node.keys.remove(key)
        count = cur_node.count - 1

        next_node = None
        if count == 0:
            pass
        elif cur_node.prev.count < count:
            next_node = DLLNode(count)
            self.insert_node(cur_node.prev, cur_node, next_node)
        else:
            next_node = cur_node.prev
        
        if next_node is not None:
            next_node.keys.add(key)
            self.key_node[key] = next_node
        else:
            del self.key_node[key]

        if len(cur_node.keys) == 0:
            self.delete_node(cur_node)

        # self.print_list()
            
    def getMaxKey(self) -> str:
        if self.tail.prev is self.head:
            return ""
        else:
            temp_node = self.tail.prev.keys.pop()
            self.tail.prev.keys.add(temp_node)
            return temp_node

    def getMinKey(self) -> str:
        if self.head.next is self.tail:
            return ""
        else:
            temp_node = self.head.next.keys.pop()
            self.head.next.keys.add(temp_node)
            return temp_node
            
    def print_list(self):
        current = self.head
        str_list = []
        while current is not None:  
            str_list.append(f'[{current.count} {current.keys}]')
            current = current.next
        print('->'.join(str_list))

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

'''
{key: Node(count, keys, prev, next)}
{count:set{(Node(key)}}
tail
head


head                        tail
(1)   
{'h'}  

{'h'}
'''
