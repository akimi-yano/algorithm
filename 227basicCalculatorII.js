// #227 basic calculator II


let input = "+1-3+ 2 * 3 *4-23";

/*
    spaces
    number
    operator
        add/subtraction
        multiplcation/division
*/
let num = 0;
let stack = []; 
let last_op = "+" 
input += "+"
for(let i = 0; i < input.length; i++){
    const character = input[i]; 
    if(character === " ")
        continue;
    else if(!isNaN(Number(character))){
        //2
        //3 -> 23
        num = num * 10 + Number(character); 
    }
    else{
        if(last_op === "*"){
            const last_num = stack[stack.length-1] 
            stack[stack.length-1] = last_num * num; 
        }
        if(last_op === "/"){
            const last_num = stack[stack.length-1] 
            stack[stack.length-1] = last_num / num; 
        }
        if(last_op === "+"){
            stack.push(num); 
        }
        if(last_op === "-"){
            stack.push(num *-1)
        }
        num = 0; 
        last_op = character; 
    }
}
console.log(stack.reduce((total,el)=> total + el));
console.log(stack); 