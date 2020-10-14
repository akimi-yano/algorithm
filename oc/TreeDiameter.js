

// Tree Diameter
// https://www.geeksforgeeks.org/diameter-of-a-binary-tree/

// Problem, Codesignal:

// You got sick because of walking in the woods at night, 
// and have to spend a week at home without going out. 
// Looking out of the window at the nearby woods you're wondering 
// if there is anything you don't yet know about them. Suddenly you 
// see a beautiful and very tall tree you haven't seen before. Since 
// you have nothing to do, you decide to examine its structure and draw
//  it in your notebook.

// You became so exited about this new tree that your temperature went 
// up, so you were forced to stay in bed. You can't see the tree from your 
// bed, but luckily you have it drawn down. The first thing you'd like to 
// find out about is the tree height. Looking at your drawing you suddenly
//  realize that you forgot to mark the tree bottom and you don't know from 
//  which vertex you should start counting. Of course a tree height can be
//   calculated as the length of the longest path in it (it is also called 
//   tree diameter). So, now you have a task you need to solve, so go ahead!

// Example

// For n = 10 and

// tree = [[2, 5], [5, 7], [5, 1], [1, 9], [1, 0], [7, 6], [6, 3], [3, 8], [8, 4]]
// the output should be treeDiameter(n, tree) = 7.



// The longest path is the path from vertex 4 to one vertex 9 or 0.

// Input/Output

// [execution time limit] 4 seconds (js)

// [input] integer n

// The number of vertices in the structure you drew in your notebook.

// Guaranteed constraints:
// 1 ≤ n ≤ 104.

// [input] array.array.integer tree

// Edges of the tree. tree[i] for each valid i contains two elements and represents an edge that connects tree[i][0] and tree[i][1].
// It is guaranteed that given graph is a tree, i.e. it is connected and has no cycles.

// Guaranteed constraints:
// tree.length = n - 1,
// tree[i].length = 2,
// 0 ≤ tree[i][j] < n.

// [output] integer

// tree diameter of the given tree.

// [JavaScript] Syntax Tips

// // Prints help message to the console
// // Returns a string
// function helloWorld(name) {
//     console.log("This prints to the console when you Run Tests");
//     return "Hello, " + name;
// }






// Your last Python3 code is saved below:
// # Find tree diameter: largest distance between any 2 nodes in the whole tree

// # 1st Abhi: 

// # no root


// # Input:
// # tree = [[2, 5], [5, 7], [5, 1], [1, 9], [1, 0], 
// # [7, 6], [6, 3], [3, 8], [8, 4]]


// Example 2
// Input:
//            5
//          /  \
//         2    1
        
// Output: 2


// # 2nd: Mahzad

// Find extremes of tree

// 2 - 5 - 7 - 6 - 3 - 8 - 4
//     |
// 0 - 1 - 9


// 2 - 4 - 0 - 9

// 2-4  
// 2-0
// 2-9
// 9-0
// 9-4
// 4-0



// tree = [[2, 5], [5, 7], [5, 1], [1, 9], [1, 0], 
//         [7, 6], [6, 3], [3, 8], [8, 4]]
    
// node_set = set()
// for x tree:
//    if x[0] in node_set:
//      node_set.add(x[0])
//    if x[1] in node_set:
//      node_set.add(x[1])
     
// n_nodes = len(node_set)  # 10

// adj_mat = [[0 for j in range(n_nodes)] for i in range(n_nodes)]

tree = [[2, 5], [5, 7], [5, 1], [1, 9], [1, 0], [7, 6], [6, 3], [3, 8], [8, 4]]
         ^ 


Map<Integer, List<Integer>> adj = new HashMap<>();


2, List<>(5)
5, List<>(2,7)
7, List<>(2,7)

5, list<>(7, 1)
1, list<>(9,0)

int[] nodes =


parent = nodes[0]
child = nodes[1]


// Solution:

//     //2 BFS approach Time O(N): a->b, b->c, return distance from b to c
//     //1. BFS from any node a to find node b furthest distance from a 
//     //2. BFS from node b to node c furthest distance from b, return distance as tree diameter
// function treeDiameter(n, tree) {
//     if(n < 4) return n-1
//     let adj = {}
//     for(let edge of tree) {
//         let node0 = edge[0]
//         let node1 = edge[1]
//         if(!adj[node0]) adj[node0] = []
//         adj[node0].push(node1)
//         if(!adj[node1]) adj[node1] = []
//         adj[node1].push(node0)
//     }
//     let first = bfsLongest(tree[0][0], adj)
//     let b = first[1].val
//     let second = bfsLongest(b, adj)
//     return second[0]
// }

// function bfsLongest(node, adj) {
//     let queue = new Queue(node)
//     let visited = new Set([])
//     visited.add(node)
//     let level = 0
//     while(queue.size > 0) {
//         let levelSize = queue.size
//         let cur = null
//         while(levelSize > 0) {
//             cur = queue.dequeue()
//             levelSize--
//             let edges = adj[cur.val]
//             for(let edge of edges) {
//                 if(!visited.has(edge)) {
//                     queue.enqueue(edge)
//                     visited.add(edge)
//                 }
//             }
//         }
//         if(queue.size > 0) {
//             level++ 
//         } else {
//             return [level, cur]
//         }
//     }
// }


// class Queue {
//     constructor(val) {
//         this.head = null
//         if(val) this.head = new LinkedList(val)
//         this.tail = this.head
//         if(this.head) this.size = 1
//         else this.size = 0
//     }
//     enqueue(val) {
//         let node = new LinkedList(val)
//         if(this.head === null) {
//             this.head = node
//             this.tail = this.head
//         } else {
//             this.tail.next = node
//             this.tail = this.tail.next
//         }
//         this.size += 1
//     }
//     dequeue() {
//         let node = this.head
//         if(this.head === null) return node
//         this.head = this.head.next
//         this.size -= 1
//         if(this.size === 0) {
//             this.head = null
//             this.tail = null
//         }
//         return node
//     }
// }

// class LinkedList {
//     constructor(val) {
//         this.val = val
//         this.next = null
//     }
// }
    



    
    

