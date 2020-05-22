function preDFS(root) {
    let result = []
    
    function traverse(curr) {
        //Base case
        if(curr == null) {
            return;
        }
        
        //Recursive steps
        result.push(curr.value);
        traverse(curr.left);
        traverse(curr.right);
    }
    traverse(root);
    
    return result;
}
