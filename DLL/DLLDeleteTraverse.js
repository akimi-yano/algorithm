// doubly linked node
class DLNode {
    constructor(data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

class DLL {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    deleteFirst(){
        let temp = this.head;
        if(this.head === this.tail) {
            this.head = null;
            this.tail = null;
        } else {
            this.head = this.head.next;
            this.head.prev.next = null;
            this.head.prev = null;
        }
        return temp;
    }

    deleteLast(){
        let temp = this.tail;
        if(this.head === this.tail) {
            this.head = null;
            this.tail = null;
        }
        else {
            this.tail.prev.next = null;
            this.tail=this.tail.prev;
            temp.prev = null;
        }
        return temp;
    }

    delete(node) {
        let runner = this.head;

        while (runner !== null) {
            if(runner === node) {
                break;
            }
            runner = runner.next;
        }

        if (runner === null){
            return null;
        } else if (runner === this.head) {
            return this.deleteFirst();
        } else if (runner === this.tail) {
            return this.deleteLast();
        } else {
            let deleted = runner;
            runner.prev.next = runner.next;
            runner.next.prev =runner.prev;
            deleted.next = null;
            deleted.prev = null;
            return deleted;
        }

    }

    frontToBackTraversal(){
        let runner = this.head;

        while(runner !== null) {
            console.log(runner.data)
            runner = runner.next;
        }
    }

    backToFrontTraversal(){
        let runner = this.tail;

        while(runner !== null){
            console.log(runner.data)
            runner =runner.prev;
        }
    }

    push(data){
        var node = new Node(data);
        if(this.head === null){
            this.head = node;
            this.tail = node;
        }else{
            node.next = this.head;
            this.head.prev = node;
            this.head = node;
        };
    }
    // append(data){}
    insertBefore(node, data){
        var runner = this.head;
        if(runner === null){
            return null;
        };
        if(runner === node){
            this.push(data);
        };
        while(runner){
            if(runner === node){
                var new_node = new Node(data);
                new_node.next = runner.next;
                new_node.prev = runner;
                runner.next = new_node;
                new_node.next.prev = new_node;
                return;
            }
            runner = runner.next;
        }
        return null;
    }
    // insertAfter(node, data){}
};