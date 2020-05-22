class Result {

    /*
     * Complete the 'treeBFS' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts TreeNode root as parameter.
     */
    public static List<Integer> treeBFS(TreeNode root) {
        //Init result list and queue
        ArrayList<Integer> res = new ArrayList<>();
        
        if(root == null) return res;
        
        Queue<TreeNode> q = new LinkedList<>();
        
        //Prime q with root node
        q.add(root);
        
        TreeNode curr;
        
        //work with queue while it's not empty
        while(q.size() >0) {
            //Dequeue front of queue to curr
            curr = q.remove();
            
            //Add curr value to result list
            res.add(curr.value);
            
            //Add children of curr node to queue
            if(curr.left != null) q.add(curr.left);
            if(curr.right != null) q.add(curr.right);
        }
        
        //return result list
        return res;
        
    }   

}

