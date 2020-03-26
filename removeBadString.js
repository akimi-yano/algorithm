// O(2N) solution
// works with space and simbols

function removeBadStrings(str1, str2){
let newStr=""
let arr=[]
for(let k=0; k<str2.length; k++){
    arr.push(str2[k])
    // console.log(arr)
}
for (let i=0; i<str1.length; i++){
    if (!(arr.indexOf(str1[i])>-1)){
        // console.log(str1[i])
        newStr+=str1[i]
        
    }
}
return newStr
}
// console.log(removeBadStrings("I have a pen", "av"))
// console.log(removeBadStrings("have a nice day!", "av"))
// console.log(removeBadStrings("have a nice day!", " "))
// console.log(removeBadStrings("have a nice day!", "!"))
console.log(removeBadStrings("have a nice day!", "have a nice day!"))
