// Stack (push, pop, isEmpty, peek, size)
// LIFO (Last In First Out)

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
    display(){
        let runner = this.top
        while (runner!= null){
            console.log(runner.data)
            runner=runner.next
        }
        return this
    }
    push(data){
        let newNode = new Node(data);
        newNode.next = this.top;
        this.top = newNode;
        this.length += 1;
        return this
    }


    pop(){
        //if stack is not empty: return top node then remove it from the stack
        if(this.isEmpty()){
            let temp = this.top;
            this.top= this.top.next;
            this.length-=1;
            return temp;
        }
        return null;

    }

  
    isEmpty(){
        //check .top
        if (this.top){
            return true;
        }
        return false;
    }

    peek(){
        return this.top;
    }
    // return top node

    size(){
        return this.length;
    }
    reverse(){
        let tempStack= new Stack()
        let runner =this.top;
        for(let i=0;i<this.length;i++){
            tempStack.push(runner.data)
            runner = runner.next;
        }
        this.top = tempStack.top;
        // tempStack.display();
        return this;
        // 1 2 3 4 5
        //new stack should be 5 4 3 2 1
    }
}

// simple node with no pointers
class SimpleNode {
    constructor(data){
        this.data = data;
    }
}

// stack class implemented with an array
class arrStack {
    constructor() {
        this.stack = [];
    }

    // push a node to the top of the stack;
    // push(data){
    //     this.stack.push(new SimpleNode(data));
    // }

    // remove and return a node from the top of the stack
    // pop(){
    //     return this.stack.pop();
    // }
    

    // // check if stack is empty
    // isEmpty(){
    //     if(this.stack.length < 1){
    //         return true;
    //     };
    //     return false;
    // }

    // return the top node if it exists,
    // not removing it from the stack
    // peek(){
    //     if(this.isEmpty()){
    //         return null;
    //     }
    //     return this.stack[this.stack.length-1];
    // }

    // check stack size
    size(){
        return this.stack.length;
    }
}

let mystack = new Stack();
mystack.push(5).push(4).push(3).push(2).push(1);
// console.log(mystack.peek());
// console.log(mystack.isEmpty());
// console.log(mystack.size())
// console.log(mystack.pop())
// mystack.display();
mystack.reverse().display();