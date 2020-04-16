// function fibonacci(n){}
// given an index of the fibonacci sequence
// return the correct value at that index.

// example sequence and indexes (n-1) + (n-2)
// 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
// 0  1  2  3  4  5  6   7   8   9  10  11   12



// a recursive function is a function that calls itself.

// a function call is equal to what that function returns

// recursive functions need a base case.
// a base case is a situation where the recursive call returns
// a value instead of a new function call.

// every time we call a recursive function, we must update the values
// to move closer and closer to the base case.

// infinite recursive calls use up all memory and cause a stack overflow.

// every function call creates it's own t diagram. unless data is passed in,
// new copies will be created.

// function calls count as variables on t diagrams.



function ten(n, string){
    n += 1;
    if(n >= 10){
        return 10;
    }
    return ten(n, string) + ten(n + 1, string);
}

ten(2, 'hello world');