public static String bfs(Vertex origin) {
        //Init result list
        String res = "";
        
        if(origin == null) return res;
        
        //Init queue, seen set
        Queue<Vertex> q = new LinkedList<>();
        HashSet<Character> seen = new HashSet<>();
        
        //Prime q with root node
        q.add(origin);
        seen.add(origin.id);
        
        Vertex curr;
        
        //work with queue while it's not empty
        while(q.size() >0) {
            //Dequeue front of queue to curr
            curr = q.remove();
            
            //Add curr value to result list
            res += curr.id;
            System.out.println(res);
            
            //Loop through neighbors and add to queue if not seen
            for(int i=0; i<curr.edges.size(); i++) {
                Vertex neighbor = curr.edges.get(i);
            // for(Vertex neighbor: curr.edges) {
                if(!seen.contains(neighbor.id)) {
                    q.add(neighbor);
                    seen.add(neighbor.id);
                }
            }
        }
        
        //return result
        return res;
    }