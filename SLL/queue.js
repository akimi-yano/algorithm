// FIFO Names -Aki, Christine, Yusuf
// first in, first out

// a queue is like the line to get into costco
// if you're at the back, it's a bummer
// if you're at the front, you got there first

// a queue only implements the following methods:
// enqueue, dequeue, front, isEmpty, size

// queues are not indexed and you can't jump
// to values in the middle or center of queues

// the only way to see all the values
// is to dequeue in a loop

class Node {
    constructor(data){
        this.data = data;
        this.next = null;
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

    enqueue(data){
let newNode = new Node(data);
if (this.back===null){
    console.log("here")
this.back = newNode;
this.front = newNode;
this.length +=1;
return this;
}
else{
    console.log("there")
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
let myQueue = new Queue();
// console.log(myQueue.isEmpty());
// console.log(myQueue.size());
myQueue.enqueue(1)
// myQueue.enqueue(1).enqueue(2).enqueue(3).display();
// console.log(myQueue.isEmpty());
// console.log(myQueue.size());
console.log(myQueue.getFront())
myQueue.enqueue(2).display();
console.log(myQueue.dequeue())
myQueue.display()

