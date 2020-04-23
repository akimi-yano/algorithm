
class Node {
    constructor(val) {
      this.val = val;
      this.next = null;
    }
}


class SList {
    constructor() {
        this.head = null;
        
    }

    addToFront(val){
    // let newnode = new Node(val);
    // newnode.next = this.head;
    // this.head = newnode;
    // return this;
    let newNode = new Node(val);
    newNode.next = this.head;
    this.head = newNode;
    return this;
    }

    // return true/false if a given list is empty
    isEmpty(){
        if(this.head == null){
            return true;
        }
        else{
            return false;
        }
    }


    // remove one node from the linked links from the front, or the head
    removeFront(){
        if (!this.isEmpty()){
    let curerntHead =  this.head;
    this.head = curerntHead.next;
        }
        return this;
    }


    // display(){}
    // loop through the list and print all values
    display(){
        let runner = this.head
        while (runner!= null){
            console.log(runner.val)
            runner=runner.next
        }
        return this
    }
}
mylist=new SList();
mylist.addToFront(5).addToFront(4).addToFront(3).addToFront(2).addToFront(1).display();
// console.log(mylist.isEmpty());
mylist.removeFront().display();