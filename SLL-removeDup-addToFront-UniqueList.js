// Akimi,

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

    removeDuplicates(){
        if(this.head === null) {
            return false;
        }

        let target = this.head.data;
        let runner = this.head;

        while(runner.next !== null) {
            if(runner.next.data === target){
                runner.next = runner.next.next;
            } else {
                runner = runner.next;
                target = runner.data;
            }
        }
    }
    // remove duplicates from a sorted linked list


    // removeNodeAfter(pointer)
    // removes node after given pointer
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

    display() {
        var runner = this.head;
        while (runner !== null) {
            console.log(runner.data);
            runner = runner.next;
        }

        return this;
    }
    addToFront(data) {
        let newNode = new Node(data);
        newNode.next = this.head;
        this.head = newNode;
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
}
function getUniques(list1, list2){
    let newList = new SList();
    let runner1 = list1.head;
    let runner2 = list2.head;
    let blacklist = [];

    while(runner1 !== null && runner2 !== null) {
        if(runner1.data < runner2.data) {
            newList.addToBack(runner1.data);
            runner1 = runner1.next;
        } else {
            newList.addToBack(runner2.data);
            runner2 = runner2.next;
        }
    }

    if(runner1 === null) {
        while(runner2 !== null) {
            newList.addToBack(runner2.data);
            runner2 = runner2.next;
        }
    } else if(runner2 === null) {
        while(runner1 !== null) {
            newList.addToBack(runner1.data);
            runner1 = runner1.next
        }
    }

    let runner = newList.head;
    let target = newList.head.data;
    while(runner.next !== null) {
        if(runner.next.data === target) {
            if(target !== blacklist[blacklist.length - 1]) {
                blacklist.push(target);
            }
        } else {
            target = runner.next.data;
        }

        runner = runner.next;
    }

    newList.removeDuplicates();

    for(let i = 0; i < blacklist.length; i++) {
        newList.delete(blacklist[i]);
    }

    return newList;

}

let myList = new SList()
myList.addToBack(1).addToBack(2).addToBack(2).addToBack(3).addToBack(5)
// myList.printVals()
// myList.removeDuplicates()
// myList.printVals()

let anotherList = new SList()
anotherList.addToBack(2).addToBack(2).addToBack(3).addToBack(4)
// anotherList.printVals()

getUniques(myList, anotherList).printVals()
