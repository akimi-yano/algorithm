// # https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

// # Given the root of a binary tree, the level of its root is 1, 
// # the level of its children is 2, and so on.

// # Return the smallest level X such that the sum of all the values 
// # of nodes at level X is maximal.

// # Input: [1,7,0,7,-8,null,null]
// # Output: 2
// # Explanation: 
// # Level 1 sum = 1.
// # Level 2 sum = 7 + 0 = 7.
// # Level 3 sum = 7 + -8 = -1.
// # So we return the level with the maximum sum which is level 2.


// # constratins 
// # time - O(2^N)
// # space - O(N)

// # of nodes : 10^4 
// # -10^5<=val<=10^5  


// # input:  root
// # output: level 

// # # [1,7,0,7,-8,null,null]
// #                 1         level 1 = 1 
// #                /\
// #               7  0        level 2  = 7
// #              /\ /\
// #             7 -8 null null level 3 = -1
            
// #           root, 1, root.val(1)
          
// #           memo = {level: sum}

// # var level = index of array

// # 0 = 1
// # 1 = 7
// # 2 = -1

// # return level + 1
          
          
// # 1 make a dictionary 
// # 2 traverse the tree keeping update the level and sum in the dictionary
// # 3 iterate the dictionary to find the max sum and its levels 
// # 4 if there are multiple levels whose sums are the same, then return the smaller level


   int maxLevelSum(TreeNode* root) {
        int h = height(root);
        vector<int> sums;
        for(int i = 1; i < h; i++){
            sums.push_back(traverse(root, i));
        }
        int level = 1, sum = sums[0];
        for(int i = 1; i < sums.size(); i++){
            if(sums[i] > sum){
                sum = sums[i];
                level = i;
            }
        }
        return level + 1;
        
    }
    int height(TreeNode* root){
        if(root == NULL)
            return 0;
        
        int lheight = height(root->left);
        int rheight = height(root->right);
        
        if(lheight > rheight){
            return lheight + 1;
        }
        else{
            return rheight + 1;
        }
    }
    int traverse(TreeNode* root, int level){
        int sum = 0;
        if(root == NULL){
            return 0;
        }
        if(level == 1){
            return root->val;
        }
        else if(level > 1){
            sum += traverse(root->left, level - 1);
            sum += traverse(root->right, level - 1);
        }
        return sum;
    }
          
            
            
            