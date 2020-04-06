class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class SLL {
    constructor() {
        this.head = null;
    }
    // addToFront(val) {
    //     let newNode = new Node(val);
    //     let currentHead = this.head;
    //     newNode.next = currentHead;
    //     this.head = newNode;
    //     return this;
    // }
    addToFront(val) {
        let newNode = new Node(val);
        newNode.next = this.head;
        this.head = newNode;
        return this;
    }
    // addArray(arr) {
    //     for (let i = 0; i < arr.length; i++) {
    //         this.addToFront(arr[i])
    //     }
    //     return this;
    // }
    addArray(arr) {
        for (let i = arr.length - 1; i >= 0; i--) {
            this.addToFront(arr[i])
        }
        return this;
    }
}
myList = new SLL();
// myList.addToFront(1).addToFront(2)
// console.log(myList)
myList.addArray([1,2,3])
console.log(myList)


// let newNode = new Node(val);
// newNode.next = this.head;
// this.head = newNode;
// return this;

// // addArray(arr) {

// }