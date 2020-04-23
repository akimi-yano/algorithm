//Names -christine, Akimi
// minStack

// recreate the Stack class as a minStack.
// minStacks support the following methods:
// push(node), pop(), peek(), isEmpty(), size()
// and a new method called
// getMin()

// getMin() should retrieve the minimum element of the stack.
// We should be able to do this in constant time with no looping!
// Just like size(), we can make this constant!
// How would we modify push and pop to keep track of a minimum element?
// Always checking if we need to update the min could be a way!


class Node {
    constructor(data){
        this.data = data;
        this.next = null;
    }
}

class minStack {
    constructor(){
        this.top = null;
        this.length = 0;
        this.mins = [];

    }

    // sense
    getMin(){
        // not sure how safe this is without error handling
        if(this.mins.length === 0){
            return null;
        }
        return this.mins[this.mins.length-1];
    }
    push(node){
        if (this.mins.length === 0 || node.data < this.getMin().data){
            this.mins.push(node);
        }
        node.next = this.top;
        this.top = node;
        this.length++;
        return this;
    };

    pop(){
        if(this.top === null){
            return null;
            // throw exception
        };

        let popped = this.top;
        this.top = this.top.next;
        popped.next = null;
        this.length--;

        if(popped.data === this.getMin().data){
            this.mins.pop();
        }

        return popped;
    }
    
    // mine
    // getMin(){
    //     if (this.top == null){
    //         return false
    //     }
    //     return this.mins[0];
    // }
    // push(data){
    //     let newNode = new Node(data);
    //     newNode.next = this.top;
    //     this.top = newNode;
    //     this.length += 1;
    //     let i=0;
    //     let minLen =this.mins.length;
    //     while (i<minLen && this.mins[i]<newNode.data){
    //         i ++;
    //     }
    //     this.mins.splice(i,0,newNode.data);
    //     return this
    // }

    // pop(){
    //     //if stack is not empty: return top node then remove it from the stack
    //     if(!this.isEmpty()){
    //         let temp = this.top;
    //         temp.next = null; //guess we need this so temp doesnt point back to the stack
    //         this.top= this.top.next;
    //         this.length-=1;
    //         this.mins.remove(temp.data);
    //         return temp;
    //     }
    //     return null;

    // }
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
// let mystack = new minStack();
// mystack.push(1);
// console.log(mystack.peek());
// console.log(mystack.isEmpty());
// console.log(mystack.size())
// console.log(mystack.pop());
// mystack.push(4).push(5);
// mystack.display();
// console.log(mystack.getMin());

let m = new minStack();
m.push(new Node(5)).push(new Node(1)).push(new Node(3)).push(new Node(0)).display();
console.log(m.getMin());
console.log(m.pop());
console.log(m.getMin());
console.log(m.pop());
console.log(m.getMin());
console.log(m.pop());
console.log(m.getMin());
console.log(m.pop());
console.log(m.getMin());



















