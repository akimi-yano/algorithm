//names: Akimi Yano, Andy, Gandolf


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

    ThirdToLast() {
        if (this.head === null || this.head.next === null)
            return null;

        var runner = this.head.next;
        var runner2 = this.head;
        while (runner.next !== null) {
            runner = runner.next;
            runner2 = runner2.next;
        }
        return runner2;
    }

    //nthFromLast(n){}
    //return the nth from last node in a given list,
    //else return the head.
    //ADVANCED CHALLENGE: Only do one traversal of your list.

    nthFromLast(n) {
        if (this.head === null){
            return this.head;
        }
        let runner1 = this.head;
        let runner2 = this.head;
        for (let i = 0; i < n; i++) {
            //if n > number of nodes in our list just return
            if (runner1 == null) {
                return
            }
            runner1 = runner1.next;
        }

        while (runner1 != null) {
            runner1 = runner1.next;
            runner2 = runner2.next;
        }
        return runner2;

    }

    //prepend(target, data){}
    //if the list has a node with the data of target, create
    //a new node (with the data of data) and attach it onto the list
    //before the target node

    prepend(target, data) {
        let prev = this.head;

        //edge case if this.head.data === target
        if (this.head.data === target) {
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
            prev = prev.next;
        }
        return this;
    }

    prepend2(target, data) {
        let prev = null;
        let current = this.head;
        while (current !== null) {
            if (current.data === target) {
                let temp = current.next;
                let newNode = new Node(data);
                newNode.next = temp;
                current.next = newNode;
            }
            prev = current;
            current = current.next;
        }

        return this;
    }

    reverse() {
        //if list is empty or only has 1 node return list
        if (this.head == null || this.head.next == null)
            return this;

        let next;
        let head = this.head;
        let prev = null;

        while (head != null) {
            //store the next node in next
            next = head.next;
            //change the current node's .next to previous
            head.next = prev;
            //set previous to the current node
            prev = head;
            //change current node to be the next node
            head = next;
        }
        //point list.head to prev (since at the end head will be null and prev will be last node in the original list)
        this.head = prev;
        return this;
    }
    //given a linked list, reverse the order of the nodes.
    //there is an optimal way to solve this algorithm, but first
    //try solving it any way that you can.

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
}