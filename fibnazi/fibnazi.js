// function Fib(n){
//     if(n==0 || n==1){
//         return n
//     }
//     else{
//         return Fib(n-2)+Fib(n-1)
//     }
// }
// console.log(Fib(5))

function BFib(n){
    if(n==0||n==1){
        return n
    }
    else if(n==2){
        return 1
    }
    else{
        return BFib(n-1)+BFib(n-2)-BFib(n-3)
    }
}

for(let i =0; i<11; i++)
console.log(BFib(i))