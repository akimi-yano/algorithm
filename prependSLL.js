class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class SList {
    constructor() {
        this.head = null;
    }

    //SList
    //complete the following methods for the SList class

    //3rdToLast(){}

    //nthFromLast(n){}
    //return the nth from last node in a given list,
    //else return the head.
    //ADVANCED CHALLENGE: Only do one traversal of your list.

    //prepend(target, data){}
    //if the list has a node with the data of target, create
    //a new node (with the data of data) and attach it onto the list
    //before the target node

    //reverse(){}
    //given a linked list, reverse the order of the nodes.
    //there is an optimal way to solve this algorithm, but first
    //try solving it any way that you can.
    nthFromLast(n) {
        if (this.head === null){
            return this.head;
        }
        let runner1 = this.head;
        let runner2 = this.head;
        for (let i = 0; i < n; i++) {
            runner1 = runner1.next;
        }

        while (runner1 != null) {
            runner1 = runner1.next;
            runner2 = runner2.next;
        }
        return runner2;

    }
    delete(data) {
        var runner = this.head;
        var prev = null;

        if (runner !== null && runner.data == data) {
            this.head = runner.next;
            return;
        }

        while (runner && runner.data !== data) {
            prev = runner;
            runner = runner.next;
        }
        if (runner === null) {
            return;
        }
        //runner is now our node to be deleted
        prev.next = runner.next;
    }
    //if data is contained within the current list, remove it.
    //consider edge cases of head node, last node, and middle nodes

    append(target, data) {
        var runner = this.head;
        if (runner === null) {
            return;
        }
        while (runner) {
            if (runner.data === target) {
                var new_node = new Node(data);
                new_node.next = runner.next;
                runner.next = new_node;
                return;
            }
            runner = runner.next;
        }
    }

    //if target is within the current list, create a new node
    //with the data of data, and append it directly after target
    addToFront(data) {
        let newNode = new Node(data);
        newNode.next = this.head;
        this.head = newNode;
        return this;
    }
    contains(data) {
        if (this.head === null) {
            return false;
        }
        var runner = this.head;
        while (runner) {
            if (runner.data === data) {
                return true
            }
            runner = runner.next;
        }
        return false;
    }

    count() {
        var count = 0;
        if (this.head === null) {
            return count;
        }
        var runner = this.head;
        while (runner) {
            count++;
            runner = runner.next;
        }
        return count;
    }

    middle() {
        var slowRunner = this.head;
        var speedyRunner = this.head;
        if (this.head === null) {
            return this.head;
        }
        while (speedyRunner !== null && speedyRunner.next !== null) {
            speedyRunner = speedyRunner.next.next;
            slowRunner = slowRunner.next;
        }
        return slowRunner;
    }

    isEmpty() {
        if (this.head === null) {
            return false;
        }
        return true;
    }

    removeFront() {
        if (!this.isEmpty()) {
            this.head = this.head.next;
            this.length--;
        }
        return this;
    }

    display() {
        var runner = this.head;
        while (runner !== null) {
            console.log(runner.data);
            runner = runner.next;
        }

        return this;
    }
    prepend(target, data) {
        let prev = this.head;
        if (this.head.data === target){
            let newHead = new Node(data);
            newHead.next = this.head;
            this.head = newHead;
            prev = prev.next;
        }
        while (prev.next != null) {

            if (prev.next.data === target) {
                let temp = prev.next;
                let newNode = new Node(data);
                newNode.next = temp;
                prev.next = newNode; 
                prev = prev.next;
            }
            prev =prev.next;
        }
        return this;
    }
}
let mylist=new SList();
mylist.addToFront(5).addToFront(4).addToFront(5).addToFront(3).addToFront(2).addToFront(1)
// console.log(mylist.nthFromLast(5));
mylist.prepend(5,6).display();