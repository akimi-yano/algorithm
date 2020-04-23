// doubly linked node
class DLNode {
    constructor(data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

class DLL {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    // the four inserts types:

    // add to head (push)
    // add to tail
    // add before a given node
    // add after a given node

    push(data){
        if (this.head== null){
            let newNode = new DLNode(data);
            this.head =newNode 
            this.tail= newNode 
            return this
        }
        let newNode = new DLNode(data);
        newNode.next = this.head
        this.head.prev = newNode
        this.head = newNode
        return this 
    }
    append(data){
        let newNode = new DLNode(data);
        this.tail.next = newNode
        newNode.prev = this.tail
        this.tail = newNode
        return this
    }

    insertBefore(node, data){
        if(this.head === null || node === this.head){
            return this.push(data);
        };

        // look for node
        let runner = this.head;
        while (runner !== null) {
            if (node === runner) {
                break;
            }
            runner = runner.next;
        }
        // node was not found
        if (runner === null) {
            console.log("node not found")
            return null;
        }

        let newPrev = new DLNode(data);
        newPrev.next = node;
        newPrev.prev = node.prev;
        node.prev.next = newPrev;
        node.prev = newPrev;
        return newPrev;

        // while (runner.next !== null){
        //     if (runner.data === node.data){
        //         let newNode = new DLNode(data)

        //         runner.prev.next= newNode
        //         newNode.next = runner
        //         let tempPrev = runner.prev
        //         runner.prev = newNode
        //         newNode.prev = tempPrev
        //     }
        //     runner= runner.next

        // }
        // if (runner.data === node.data){
        //     let newNode = new DLNode(data)

        //     runner.prev.next= newNode
        //     newNode.next = runner
        //     let tempPrev = runner.prev
        //     runner.prev = newNode
        //     newNode.prev = tempPrev
        // }
        // return this
    }
    
        // insertBefore(node, data){
        //     var runner = this.head;
        //     if(runner === null){
        //         return null;
        //     };
        //     if(runner === node){
        //         this.push(data);
        //     };
        //     while(runner){
        //         if(runner === node){
        //             var new_node = new Node(data);
        //             new_node.next = runner.next;
        //             new_node.prev = runner;
        //             runner.next = new_node;
        //             new_node.next.prev = new_node;
        //             return;
        //         }
        //         runner = runner.next;
        //     }
        //     return null;
        // }

    insertAfter(node, data){
        if(this.tail === null || node === this.tail){
            return this.append(data);
        };

        // look for node
        let runner = this.head;
        while (runner !== null) {
            if (node === runner) {
                break;
            }
            runner = runner.next;
        }
        // node was not found
        if (runner === null) {
            console.log("node not found")
            return null;
        }

        let newNext = new DLNode(data);
        newNext.prev = node;
        newNext.next = node.next;
        node.next.prev = newNext;
        node.next = newNext;
        return newNext;

    }

    display(){
        let runner = this.head
        while (runner!= null){
            console.log(runner.data)
            runner=runner.next
        }
        return this
    }

}

let myList = new DLL()
myList.push(1)
// console.log(myList)
// myList.display()
myList.append(2)
// myList.display()
myList.push(3)
// myList.display()

// check the insert before
// myList.insertBefore(myList.tail.prev, 5)
// myList.insertBefore(myList.head.next, 5)
// myList.insertBefore(myList.tail, 5)
// myList.insertBefore(myList.head, 5)
// myList.insertBefore(new DLL(null), 5)
// myList.display()


// myList.insertAfter(myList.head, 8)
// myList.insertAfter(myList.tail.prev, 8)
// myList.insertAfter(myList.head.next, 8)
// myList.insertAfter(myList.tail, 8)
// myList.insertAfter(new DLL(null), 8)
myList.display()























