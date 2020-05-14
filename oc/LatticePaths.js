/*
 * Complete the 'latticePaths' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER m
 *  2. INTEGER n
 */

function latticePaths(m, n) {
    
    //Bottom-up helper method recursion from 0,0 to m,n
    function helper(row, col) {
        //Base cases
        //1. Boundary Breached
        if(row > m || col > n) return 0;
        
        //2. Destination Reached
        if(row == m && col == n) return 1;
        
        //Return sum of recursive actions
        return helper(row+1, col) + helper(row, col+1);
    }
    
    return helper(0,0);
    
    
    //Top-down pure recursion from m,n to 0,0
//     //Base cases
//     //1. Boundary Breached
//     if(m < 0 || n <0) return 0;
//     //2. Destination Reached
//     if(m == 0 && n == 0) return 1;
    
//     //Return sum of recursive actions
//     return latticePaths(m-1, n) + latticePaths(m, n-1);
    
    //Top-down pure recursion one-liner
    // return m == 0 || n == 0 ? 1 : latticePaths(m-1, n) + latticePaths(m, n-1);
    
}

