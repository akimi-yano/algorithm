
// LEVEL1 O(N*K) (k is string's length)
function rotateString(str,n){
let length = str.length
if (n===0){
    return str
}
else{
    return rotateString((str.substring(length-1) + str.substring(0,length-1)), n-1)
}
}
console.log(rotateString("abcdefg",8))

// LEVEL1 O(K+N) solutiuon (k is string's length)
function rotateStringTwo(str,n){
    let strArr = [];
    let shift = str.length - (n % str.length)
    for (let i = 0; i < str.length; i++) {
        let pos = (i + shift) % str.length
        strArr[i] = str[pos]
    }
    return strArr.join('')
}
console.log(rotateStringTwo("abcdefg", 8))

// LEVEL2
// function isRotation(str1, str2){

// return (str1.length == str2.length && (str1+str1).includes(str2))

// }
// console.log(isRotation("ab", "ba"))
