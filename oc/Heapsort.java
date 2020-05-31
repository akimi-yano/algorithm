class Result {

    /*
     * Complete the 'heapsort' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static List<Integer> heapsort(List<Integer> arr) {
        //Bubble down heapify array
        for(int p = (arr.size()-1)/2; p>= 0; p--) {
            bubbleDown(arr, p, arr.size());
        }
        
        //Convert max heap to sorted array
        for(int heapEnd = arr.size()-1; heapEnd > 0; heapEnd--) {
            swap(arr, 0, heapEnd);
            bubbleDown(arr, 0, heapEnd);
        }
        
        
        //return the same array as input
        return arr;
    }
    
    private static void bubbleDown(List<Integer> arr, int parent, int heapSize) {
        //Calculate child index with greater value
        int child = getChild(arr, parent, heapSize);
        
        //while child index is valid and parent value is < child value
        while(child < heapSize && arr.get(parent) < arr.get(child)) {
        
            //Swap parent and child values
            swap(arr, parent, child);
        
            //Shift parent pointer to child pointer
            parent = child;
        
            //Calc new child pointer
            child = getChild(arr, parent, heapSize);
            
        }
    }
    
    private static int getChild(List<Integer> arr, int parent, int heapSize) {
        int child1 = 2*parent+1;
        int child2 = 2*parent+2;
        
        //Child1 index is invalid
        if(child1 >= heapSize) return child1;
        
        
        //Child2 index is invalid but child1 is valid
        if(child2 >= heapSize) return child1;
        
        
        //Both indices are valid
        return arr.get(child1) > arr.get(child2) ? child1 : child2;
        
    }
    
    
    private static void swap(List<Integer> arr, int ind1, int ind2) {
        int temp = arr.get(ind1);
        arr.set(ind1, arr.get(ind2));
        arr.set(ind2, temp);
    }

}

