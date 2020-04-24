class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

// Partitioning a linked list around a given value, keeping original order.

// Input : 1->4->3->2->5->2->3,
//         x = 3
// Output: 1->2->2->3->3->4->5

// Input : 1->4->2->10
//         x = 3
// Output: 1->2->4->10

// Input : 10->4->20->10->3
//         x = 3
// Output: 3->10->4->20->10

// Given a value x
// partition a linked list so that all nodes less than x come first, or to the left
// then all nodes with value equal to x
// finally nodes with value greater than or equal to x to the right

// The original relative order of the nodes in each of the three partitions should be preserved.
// The partition must work in-place.

class SList {
    constructor() {
        this.head = null;
    }

    removeDuplicates(){
        var runner = this.head;
        var temp = runner;
        while(runner){
            while(temp !== null && temp.data === runner.data){
                temp = temp.next;
                //
            }
            runner.next = temp;
            runner = temp;
        }
    }

    nthFromLast(n) {
        if (this.head === null) {
            return this.head;
        }
        var runnerFast = this.head;
        var runnerSlow = this.head;
        var count = 0;
        while (runnerFast) {
            if (count >= n) {
                runnerSlow = runnerSlow.next;
            }
            runnerFast = runnerFast.next;
            count++;
        }
        return runnerSlow;
    }

    nthFromLast2(n) {
        if (this.head === null) {
            return this.head;
        }
        var runner = this.head;
        while (n > 0) {
            runner = runner.next;
            n--;
        }
        var secondRunner = this.head;
        while (runner) {
            runner = runner.next;
            secondRunner = secondRunner.next;
        }
        return secondRunner;
    }

    reverse() {
        var prev = null;
        var current = this.head;
        var next = null;
        while (current) {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        this.head = prev;
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
    printVals(){
        let runner = this.head
        while (runner!= null){
            console.log(runner.data)
            runner=runner.next
        }
        return this
    }
    addToBack(data){
        let newNode = new Node(data);
        let runner = this.head
        if (this.head === null){
            this.head = newNode
        } else {
            while (runner.next!=null){
                runner = runner.next
            }
            runner.next = newNode
        }
    return this
}
partition(data){

    let beforeStart = null
    let beforeEnd = null
    let middleStart = null
    let middleEnd = null

    let afterStart= null
    let afterEnd= null

    let runner= this.head


    while(runner!=null){
        if(runner.data<data){
            if(beforeStart==null){
                beforeStart = runner
                beforeEnd =runner

            }
            else{
                beforeEnd.next = runner;
                beforeEnd = runner;
            }
        }
        if(runner.data===data){
            if(middleStart==null){
                middleStart = runner
                middleEnd =runner
            }
            else{
                middleEnd.next = runner
                middleEnd = runner
            }
        }
        if(runner.data>data){
            if(afterStart==null){
            afterStart = runner
            afterEnd =runner
        }
        else{
            afterEnd.next = runner;
            afterEnd = runner;
        }
    }
    runner = runner.next
    }
if(beforeEnd!= null){
    if (middleStart !== null) {
        beforeEnd.next = middleStart
    } else if (afterStart !== null) {
        beforeEnd.next = afterStart
    } else {
        beforeEnd.next = null
    }
}
if(middleEnd!=null){
    middleEnd.next=afterStart
}
if(afterEnd!=null){
    afterEnd.next = null
}


if(beforeStart != null){
    this.head=beforeStart
}
else if (middleStart!=null){
    this.head=middleStart
}
else{
    this.head=afterStart
}

return this.head
}
}
let myList = new SList()
// 1->4->3->2->5->2->3,
// 1->4->2->10
// 10->4->20->10->3
// myList.addToBack(1).addToBack(4).addToBack(3).addToBack(2).addToBack(5).addToBack(2).addToBack(3)
// myList.addToBack(1).addToBack(4).addToBack(2).addToBack(10)
myList.addToBack(10).addToBack(4).addToBack(20).addToBack(10).addToBack(3)
myList.printVals()
console.log("***********")
myList.partition(3)
myList.printVals()