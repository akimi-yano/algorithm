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
    addToFront(val) {
        let newNode = new Node(val);
        let currentHead = this.head;
        newNode.next = currentHead;
        this.head = newNode;
        return this;
    }
    addArray(arr) {
        for (let i = 0; i < arr.length; i++) {
            this.addToFront(arr[i])
        }
        return this;
    }

    //Building on the previous Linked List algorithms, please complete
    //the following methods.

    //contains(data){}
    //given data, traverse the current list and return true if that
    //data is present in our list, else return false

    containsData(val) {
        let runner = this.head;
        if(runner === null) {
            return false;
        }
        while(runner !== null) {
            if(runner.val === val) {
                return true;
            }
            runner = runner.next;
        }
        return false;
    }
    //count(){}
    //return the total number of nodes in the current list

    count(){
        let runner = this.head;
        let count = 0;
        if (runner === null){
            return count;
        }
        while (runner !== null){
            runner = runner.next;
            count= count +1;
        }
        return count;
    }
    //middle(){}
    //if odd, return the middle node of a list. return the node, not
    //the value, if even return head

    middle(){
        let fastRunner =this.head;
        let slowRunner =this.head;
        while (fastRunner.next !== null){
            //even
            if(fastRunner.next.next === null) {
                return this.head;
            }
            //odd
            fastRunner=fastRunner.next.next;
            slowRunner=slowRunner.next;
        }
        return slowRunner;
    }
    //BONUS
    //rotateFrontAndBack(){}
    //if the total number of nodes in a linked list are 2 or more,
    //swap the head with the last node on the list.
    
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

}
    //ADVANCED BONUS
    //recursiveContains(data, runner){}
    //try to refactor contains with a function that calls itself


myList = new SLL();
myList.addArray([8,2,3,4,9,2,4])

let runner = myList.head
while(runner !== null) {
    console.log("first",runner.val)
    runner = runner.next
}

console.log(myList.containsData(3))
console.log(myList.count())
console.log(myList.middle())
console.log(myList.rotateFrontandBack())

let runner2 = myList.head
while(runner2 !== null) {
    console.log("reversed",runner2.val)
    runner2 = runner2.next
}