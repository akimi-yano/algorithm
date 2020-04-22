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
        if (this.head== null){
            let newNode = new DLNode(data);
            this.head =newNode 
            this.tail= newNode 
            return this
        }
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
    deleteFirst(){
        let temp = this.head;
        if(this.head === this.tail) {
            this.head = null;
            this.tail = null;
        } else {
            this.head = this.head.next;
            this.head.prev.next = null;
            this.head.prev = null;
        }
        return temp;
    }
    deleteLast(){
        let temp = this.tail;
        if(this.head === this.tail) {
            this.head = null;
            this.tail = null;
        }
        else {
            this.tail.prev.next = null;
            this.tail=this.tail.prev;
            temp.prev = null;
        }
        return temp;
    }

    delete(node) {
        let runner = this.head

        while (runner !== null) {
            if(runner === node) {
                break;
            }
            runner = runner.next
        }

        if (runner === null){
            return null
        } else if (runner === this.head) {
            return this.deleteFirst();
        } else if (runner === this.tail) {
            return this.deleteLast();
        } else {
            let deleted = runner
            runner.prev.next = runner.next
            runner.next.prev =runner.prev
            deleted.next = null
            deleted.prev = null
            return deleted
        }

    }
    frontToBackTraversal(){
        let runner = this.head;

        while(runner !== null) {
            console.log(runner.data)
            runner = runner.next;
        }
    }

    backToFrontTraversal(){
        let runner = this.tail;

        while(runner !== null){
            console.log(runner.data)
            runner =runner.prev;
        }
    }
    isPalindrome(){
        if(this.head === null) {
            return false;
        }

        let runner1 = this.head;
        let runner2 = this.tail;

        while(runner1 !== null) {
            if(runner1.data !== runner2.data) {
                return false;
            }
            runner1 = runner1.next;
            runner2 = runner2.prev;
        }

        return true;
    }
    // return true or false if the DLL is a palindrome

    reverse(){
        if(this.head === null) {
            return false;
        }

        this.head = this.tail;
        let runner = this.head;
        while(runner !== null) {
            let temp = runner.next;
            runner.next = runner.prev;
            runner.prev = temp;

            if(runner.next === null){
                this.tail = runner;
            }

            runner = runner.next;
        }
    }
    // reverse a Doubly Linked List.

    // - you must move the nodes, not the data (different from BST)
    // - reverse returns nothing


}
// harder challenge

// function DLLisRotation(DLL1, DLL2){
//     let newList = new DLL();

//     // makes a doubled copy of DLL2
//     for(let i = 0; i < 2; i++) {
//         let runner = DLL2.head;
//         while(runner !== null) {
//             newList.append(runner.data)
//             runner = runner.next;
//         }
//     }

//     let runner1 = DLL1.head;
//     let runner2 = newList.head;
//     while(runner2 !== null && runner1 !== null) {
//         if(runner1.data === runner2.data) {
//             runner1 = runner1.next;
//         } else {
//             runner1 = DLL1.head;
//         }

//         runner2 = runner2.next;
//     }

//     return runner1 === null;

// }
// return true or false if DLL1 is a rotation of DLL2

// DLL1 = (1)  (2)  (3)  (4)
// DLL2 = (4)  (1)  (2)  (3)

function DLLisRotation(DLL1, DLL2){
    // let newList = new DLL();

    // // makes a doubled copy of DLL2
    // for(let i = 0; i < 2; i++) {
    //     let runner = DLL2.head;
    //     while(runner !== null) {
    //         newList.append(runner.data)
    //         runner = runner.next;
    //     }
    // }

    let runner1 = DLL1.head;
    let runner2 = DLL2.head;
    let looped = false;
    let counter1 = 0;
    let counter2 = 0;

    while(runner1!== null){
        counter1+=1;
        runner1=runner1.next;
    }

    while(runner2!== null){
        counter2+=1;
        runner2=runner2.next;
    }
    if (counter1!==counter2){
        return false;
    }

    while(runner2 !== null && runner1 !== null) {
        if(runner1.data === runner2.data) {
            runner1 = runner1.next;
        } else {
            runner1 = DLL1.head;
        }

        if(runner2.next === null && !looped) {
            looped = true;
            runner2 = DLL2.head;
        } else {
            runner2 = runner2.next;
        }
    }

    return runner1 === null;

}


let myList = new DLL()

// console.log(myList)
// myList.display()
myList.append(1)
myList.append(2)
// myList.display()
myList.append(3)
// myList.display()

// console.log(myList)
// myList.display()
// myList.push(3)
// // myList.display()
// myList.push(2)
// myList.push(1)

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
// myList.delete(myList.head.next)
// console.log(myList.delete(myList.head.next))
// console.log(myList.delete(myList.head))
// console.log(myList.delete(myList.tail))
// myList.display()
console.log("********")
// myList.frontToBackTraversal()
// myList.backToFrontTraversal()
// console.log(myList.isPalindrome())

// myList.reverse()
// myList.display()
let anotherList = new DLL()
anotherList.append(1).append(2).append(3)
anotherList.display()
console.log(DLLisRotation(myList, anotherList))




















