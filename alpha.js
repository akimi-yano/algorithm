// Part 1 Challenge
// is Pangram
// Write a standalone function that checks whether a given string contains all letters in the English alphabet, upper or lowercase.
// Given: "How quickly daft jumping zebra vex"
// => true
// Given: "John quickly extemporized five tow bags"
// => true
// Given: "apple sauce"
// => return false
// // strings must be minimum 26 characters long or else there's no reason to finish checking.
// // Part 2 Challenge
// all Permutation
// Create a standalone function that accepts a string and returns all permutations of that string. Use recursion!
// Given: "ABC"
// => ["ABC", "ACB", "BCA", "BAC", "CAB", "CBA"]
function isPangram(str) {
    if (str.length < 26) {
        return false
    }
    let dict = {}
    let alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    str = str.toLowerCase();
    for (let i = 0; i < alpha.length; i++) {
        dict[alpha[i]] = true;
    }
    console.log(Object.keys(dict))

    for (let k = 0; k < str.length; k++) {
        if (str[k] in dict) {
            delete dict[str[k]]
        }
    }
    console.log(Object.keys(dict))
    if (Object.keys(dict).length !== 0) {
        return false
    }
    else {
        return true
    }


}
// console.log(isPangram("Abcdefghijklmnopqrstuvwxyz"))
// console.log(isPangram("How quickly daft jumping zebras vex"))
// // console.log(isPangram("John quickly extemporized five tow bags"))
// console.log(isPangram("apple sauce"))

// function permutation(str){
// if (str.length<=1){
//         return [str]
// }
// let arr=[]
// for (let i=0; i<str.length; i++){
//     let firstLetter=str[i]
//     // console.log(firstLetter)
//     substring =str.substring(0,i)+str.substring(i+1,str.length)
//     // console.log(substring)
//     let subPerm = permutation(substring)
//     for(k=0; k<subPerm.length; k++){
//         arr.push(firstLetter+subPerm[k])
//     }
// }
// return arr
// }
// console.log(permutation("ABC"))
// console.log(permutation("abcd"))

// goal : ["ABC", "ACB", "BCA", "BAC", "CAB", "CBA"]


function isPan(str) {
    let dict = {
        'a': 1,
        'b': 1,
        'c': 1,
        'd': 1,
        'e': 1,
        'f': 1,
        'g': 1,
        'h': 1,
        'i': 1,
        'j': 1,
        'k': 1,
        'l': 1,
        'm': 1,
        'n': 1,
        'o': 1,
        'p': 1,
        'q': 1,
        'r': 1,
        's': 1,
        't': 1,
        'u': 1,
        'v': 1,
        'w': 1,
        'x': 1,
        'y': 1,
        'z': 1,
    }
    for (let i = 0; i < str.length; i++) {
        if (str[i].toLowerCase() in dict) {
            delete dict[str[i].toLowerCase()];
        }
        if (Object.keys(dict).length === 0) {
            return true
        }
    }
    return false
}
console.log(isPan("How quickly daft jumping zebras vex"))
function getAnagrams(string, memo, arr) {
    var strlen = string.length;
    if (!memo) { memo = ""; }
    if (!arr) { arr = []; }
    if (strlen === 0) {
        arr.push(memo);
    }
    for (var i = 0; i < strlen; i++) {
        getAnagrams(string.substring(0, i) + string.substring(i + 1, strlen), memo + string[i], arr);
    }
    return arr;
}
var input = "dog";
console.log(getAnagrams(input));

