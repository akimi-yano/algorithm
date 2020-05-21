function reverseLinkedList(node) {
    let prev = null;
    let curr = node;
    let next;
    
    while(curr != null) {
        //Set aside next temp variable
        next = curr.next;
        curr.next = prev;
        prev = curr;
        //Make use of temp variable to shift curr on
        curr = next;
    }
    return prev;
}



function swapNodes(head, a, b) {
    //Check if a == b
    if(a == b) return head;
    
    //Search for a and b nodes
    let aNodes = search(head,a);
    let bNodes = search(head,b);
    
    let pA = aNodes[0];
    let cA = aNodes[1];
    let pB = bNodes[0];
    let cB = bNodes[1];
    
    //Check that both nodes found
    if(cA == null || cB == null) return head;
    
    
    //Check if cA or cB is head and do relevant swaps
    //Check if cA is head
    if(pA == null) {
        pB.next = cA;
        head = cB;
    }
    //Check if cB is head
    else if(pB == null) {
        pA.next = cB;
        head = cA;
    }
    //Neither node is head, so swap normally
    else {
        pA.next = cB;
        pB.next = cA;
    }
    
    
    //Swap next pointers of cA and cB using temp pointer
    let temp = cA.next;
    cA.next = cB.next;
    cB.next = temp;
    
    //Swap next pointers of cA and cB using native js operations
    // [cA.next, cB.next] = [cB.next, cA.next];
    
    //return head node
    return head;
    
    
    function search(node, val) {
        let prev = null;
        let curr = node;
        
        while(curr != null) {
            if(curr.data == val) {
                return [prev, curr]; //if at head node (and data is '1'), then return will be [null, 1]
            }
            prev = curr;
            curr = curr.next;
        }
        
        return [null, null];
    }

}


function isCircular(node) {
    let tortoise = node;
    let hare = node;
    
    //Tortoise and hare nodes move at different paces through LL
    while(hare != null && hare.next != null) {
        hare = hare.next.next;
        tortoise = tortoise.next;
        if(hare === tortoise){
            return true;
        }
    }
    //If while loop exits naturally, we know the list terminates
    return false;
    
}