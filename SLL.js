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
    addToFront(data) {
        let newNode = new Node(data);
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
    printVals(){
        let runner = this.head
        while (runner!= null){
            console.log(runner.val)
            runner=runner.next
        }
        return this
    }
    delete(data){
        //when runner 1 gets to data, it goes to the next,and runner two is set to that data, so they are connected.
        // edge cases
        if (this.head.val===data){
            console.log("here")
        this.head = this.head.next;
        return this;
        }
        // if (this.head.data===data){
        //     let currentHead = this.head;
        //     this.head=currentHead.next;
        // return this;
        
        let runner1=this.head.next;
        let runner2=this.head;
        
        while(runner1.val!=data && runner1.next!=null){
            runner1=runner1.next
            runner2=runner2.next
        }
        if (runner1.next!=null){
        runner1=runner1.next;
        runner2.next=runner1;
        return this;
        }
        else{
        runner2.next=null;
        return this;
        }
        }
}
myList = new SLL();
myList.addToFront(3).addToFront(2).addToFront(1)
// console.log(myList)
// myList.addArray([1,2,3])
myList.printVals()
myList.delete(1)
myList.printVals()
// console.log(myList)


// let newNode = new Node(val);
// newNode.next = this.head;
// this.head = newNode;
// return this;

// // addArray(arr) {

// }