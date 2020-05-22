/*
 * Complete the 'find_all_paths' function below.
 *
 * The function is expected to return a STRING_ARRAY.
 * The function accepts following parameters:
 *  1. Vertex origin
 *  2. String destination
 */

/*
 * For your reference:
 *
 * Vertex {
 *   char id;
 *   edges[Vertex];
 * }
 *
 */

function find_all_paths(origin, destination) {
    //Init a seen set and result list
    let seen = new Set();
    let result = [];
    
    function dfs(curr, path) {
        //Append to path string and add to seen set
        path += curr.id;
        seen.add(curr.id);
        
        //Check if destination is reached (Base case)
        if(curr.id == destination) {
            result.push(path);
        } else {
            //Loop through edges
            for(let neighbor of curr.edges) {
                if(!seen.has(neighbor.id)) {
                    //Dfs from neighbor node and path str so far
                    dfs(neighbor, path);
                }
            }
        }
        seen.delete(curr.id);
    }
    
    
    dfs(origin, "");
    
    return result;

}

