

// #1 Compare Queues
function isEqual(queue1, queue2) {
    if (queue1.size() !== queue2.size()) {
        return false;
    }

    let result = true;

    for (let i = 0; i < queue1.size(); i++) {
        let pop1 = queue1.dequeue();
        let pop2 = queue2.dequeue();

        if (pop1.data !== pop2.data) {
            result = false;
        }

        queue1.enqueue(pop1.data);
        queue2.enqueue(pop2.data);
    }

    return result;
}

// given two queues, return true or false if the queues are equal.

// a queue of nodes is a complex data structure of pointers, you must
// return both queues back to their original order.

// you may only use the standard queue interfaces enqueue dequeue peek
// isEmpty, and size.



// #2 Queue: isPalindrome

// function isPalindrome(queue){}

// given a queue, return true or false if that queue is a palindrome.
// ie: is equal to itself even if the order is reversed
// 1 2 3 4 5 4 3 2 1

// you must return the queue back to it's original order.

function isPalindrome(queue) {
    let arr = [];

    for (let i = 0; i < queue.size(); i++) {
        let pop = queue.dequeue();
        arr.push(pop.data);
        queue.enqueue(pop.data);
    }

    console.log(arr)

    for (let i = 0; i < Math.floor(arr.length) / 2; i++) {
        if (arr[i] !== arr[arr.length - 1 - i]) {
            return false;
        }
    }

    return true;
}

class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

// LIFO
class Stack {
    constructor() {
        this.top = null;
        this.length = 0;
    }

    push(data) {
        var newNode = new Node(data);
        newNode.next = this.top;
        this.top = newNode;
        this.length++;
    };

    pop() {
        if (this.top === null) {
            return null;
            // throw exception
        };

        var node = this.top;
        this.top = this.top.next;
        node.next = null;
        this.length--;

        return node;
    }

    isEmpty() {
        if (this.top === null) return true;
        return false;
    }

    peek() {
        return this.top;
    }

    size() {
        return this.length;
    }
}

// FIFO
class Queue {
    constructor() {
        this.back = null;
        this.front = null;
        this.length = 0
    }

    enqueue(data) {
        var newNode = new Node(data);
        if (this.back === null) {
            this.back = newNode;
            this.front = newNode
        } else {
            this.back.next = newNode;
            this.back = newNode;
        }
        this.length+=1;
        return this;
    }

    dequeue() {
        if (this.front === null) {
            return null;
        };
        if (this.front === this.back) {
            this.back = null;
        };
        let returnNode = this.front;
        this.front = returnNode.next;
        returnNode.next = null;
        this.length-=1;
        return returnNode;
    }

    peek() {
        return this.front;
    }

    isEmpty() {
        if (this.front && this.back) return false;
        return true;
    }

    size() {
        return this.length;
    }
}
let queueOne = new Queue();
queueOne.enqueue(1).enqueue(2).enqueue(3).enqueue(4).enqueue(5)
console.log(queueOne.peek())

let queueTwo = new Queue();
queueTwo.enqueue(1).enqueue(2).enqueue(3).enqueue(4).enqueue(5)
console.log(queueTwo.peek())


console.log(isEqual(queueOne, queueTwo))
console.log(queueOne.peek())
console.log(queueTwo.peek())

let queue = new Queue();
queue.enqueue(1).enqueue(2).enqueue(3).enqueue(2).enqueue(1)
console.log(queue.peek())
console.log(isPalindrome(queue))
console.log(queue)
