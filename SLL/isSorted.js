// Stack: is Sorted

// isSorted(){}

// using only one additional stack or queue as storage (or a temp), check true or false if a stack
// is a sorted smallest to greatest collection of numbers.

// must return the stack back to it's original order when we are done.

// you may not linearly iterate through the stacks and queues

// if you want to see all the values, you need to run pop() or dequeue() until you can't.

class Node {
    constructor(data){
        this.data = data;
        this.next = null;
    }
}

class Stack {
    constructor(){
        this.top = null;
        this.length = 0;
    }

    reverse(){
        let tempStack= new Stack()
        let runner =this.top;
        for(let i=0;i<this.length;i++){
            tempStack.push(runner.data)
            runner = runner.next;
        }
        this.top = tempStack.top;
        return this;
        // 1 2 3 4 5
        //new stack should be 5 4 3 2 1
    }

    push(node){
        node.next = this.top;
        this.top = node;
        this.length += 1;
        return this;
    }

    pop(){
        //if stack is not empty: return top node then remove it from the stack
        if(!this.isEmpty()){
            let temp = this.top;
            this.top= this.top.next;
            temp.next = null; 
            this.length-=1;
            return temp;
        }
        return null;

    }
//return true if it empty
    isEmpty(){
        if (this.top){
            return false;
        }
        return true;
    }


    peek(){
        // return top node
        return this.top;
    }


    size(){
        return this.length;
    }
    display(){
        let runner = this.top
        while (runner!= null){
            console.log(runner.data)
            runner=runner.next
        }
        return this
    }
}

class Queue {
    constructor(){
        this.back = null;
        this.front = null;
        this.length = 0
    }

    // it is possible to implement all of these methods
    // without linearly iterating through the queue. like
    // the stack, we want these methods to have the same runtime
    // no matter how large we make the queue

    enqueue(newNode){
        if (this.back===null){
            this.back = newNode;
            this.front = newNode;
            this.length +=1;
            return this;
        }
        else{
            this.back.next = newNode;
            this.back=newNode;
            this.length+=1;
            return this;
        }
}
    // add a node to the back

    dequeue(){

        if (this.front===null){
        return false
        }
        //when there is one node
        if(this.front === this.back){
            this.back = null;
        };
        let returnNode = this.front 
        this.front = returnNode.next;
        //disconnecting the tempnode's connection
        returnNode.next = null;
        this.length -=1
        return returnNode
        
    }
    // remove and return a node from the front

    getFront(){
    if (this.front === null){
        return "queue is empty"
    }
    return this.front
    }
    // return the front node, not removing it

    isEmpty(){
        if (this.back=== null || this.front===null){
        return true
        }
        else{
        return false
        }
    }
    // is the queue empty, true or false?

    size(){
        return this.length;
    }
    // how many nodes are in our queue?
    display(){
        let runner = this.front
        while (runner!= null){
            console.log(runner.data)
            runner=runner.next
        }
        return this
    }
}
function copy(stack1) {
    let queue = new Queue();
    let newStack = new Stack();

    while (!stack1.isEmpty()) {
        newStack.push(stack1.pop());
    }

    while (!newStack.isEmpty()) {
        queue.enqueue(newStack.pop());
    }

    while (!queue.isEmpty()) {
        let temp = queue.dequeue();
        let newNode = new Node(temp.data);

        stack1.push(temp);
        newStack.push(newNode);
    }

    return newStack;
}
// stack class implemented with an array


function isSorted(stack1){
    if (stack1.isEmpty()) {
        return true;
    }

    let result = true;
    let temp = stack1.pop();
    let val = temp.data;
    let newStack = new Stack();
    newStack.push(temp);
    // console.log(stack1.isEmpty())

    while (!stack1.isEmpty()) {
        temp = stack1.pop();
        // console.log(val, temp.data)
        if (temp.data >= val) {
            val = temp.data;
            newStack.push(temp);
        } else {
            stack1.push(temp);
            result = false;
            break;
        }
    }

    while (!newStack.isEmpty()) {
        stack1.push(newStack.pop());
    }

    return result;
}


// let mystack = new Stack();
// mystack.push(new Node(3)).push(new Node(2)).push(new Node(1))
// // mystack.display()
// console.log(isSorted(mystack))
// let myStack = new Stack();
// myStack.push(new Node(1)).push(new Node(2)).push(new Node(3))
// console.log(isSorted(myStack))
// // mystack.display()
// // myStack.display()
// let stack3 = new Stack();
// stack3.push(new Node(0)).push(new Node(0))
// console.log(isSorted(stack3))

let stack1 = new Stack();
stack1.push(new Node(3)).push(new Node(2)).push(new Node(1));
let stack2 = stack1;
//let newStack = copy(stack1);
//newStack.pop();
stack2.pop();
stack1.display();
stack2.display();



// other data structures to note:

// circQueue
// circular queue is a linear data structure using first in first out.
// the last position is connected to the front, making a circle.
// this position is sometimes called the ring buffer.
// circular queues have a .length property, which fixes the size of our queue

// circular queues hae the following methods
// peekFront, peekBack, enqueue(node), dequeue, isempty, isfull

// and the following attributes
// front, back, length


// priority queue
// a queue that has both a value and a priority.
// a priority queue implements: getHighestPriority, dequeueHighestPriority
// these methods run at O(n)