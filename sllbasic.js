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

    //Building on the previous Linked List algorithms, please complete
    //the following methods.

    //contains(data){}
    //given data, traverse the current list and return true if that
    //data is present in our list, else return false

    //count(){}
    //return the total number of nodes in the current list

    //middle(){}
    //if odd, return the middle node of a list. return the node, not
    //the value, if even return head

    //BONUS
    //rotateFrontAndBack(){}
    //if the total number of nodes in a linked list are 2 or more,
    //swap the head with the last node on the list.

    //ADVANCED BONUS
    //recursiveContains(data, runner){}
    //try to refactor contains with a function that calls itself

    isEmpty(){
        if(this.head === null){
            return false;
        }
        return true;
    }

    removeFront(){
        if(!this.isEmpty()){
            this.head = this.head.next;
            this.length--;
        }
        return this;
    }

    display(){
        var runner = this.head;
        while(runner !== null){
            console.log(runner.data);
            runner = runner.next;
        }

        return this;
    }
    addToFront(val) {
        let newNode = new Node(val);
        let currentHead = this.head;
        newNode.next = currentHead;
        this.head = newNode;
        return this;
    }
    // rotateFrontandBack() {
    //     let runner = this.head;
    //     let tempNext = this.head.next;
    //     while (runner.next.next != null){
    //         runner = runner.next
    //     }
        
    //     // runner is the second to last
    //     let tempLast = runner.next;
    //     runner.next=this.head;
    //     tempLast.next = tempNext;
    //     this.head = tempLast;

    //     return this;
    // }

    rotateFrontandBack() {
        let runner = this.head;
        let tempHead = this.head;
        while (runner.next.next !== null){
            runner = runner.next
        }
        
        runner.next.next = this.head.next;
        this.head = runner.next;
        runner.next = tempHead;
        tempHead.next = null;
        return this
    }

    display(){
        var runner = this.head;
        while(runner !== null){
            console.log(runner.val);
            runner = runner.next;
        }

        return this;
    }

    

}
myList = new SList()
myList.addToFront(5).addToFront(4).addToFront(3).addToFront(2).addToFront(1).display()
myList.rotateFrontandBack().display()
