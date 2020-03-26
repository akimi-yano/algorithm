// sensei answers

function censor(A, B) {
    console.log(A);
    var uniques = {};
    for(var i=0; i<B.length; i++) {
        if(B[i] in uniques) {
            B[i] ++;
        } else {
            uniques[B[i]] = 0;
        }
    }
    for(var j=0; j<A.length; j++) {
        if(A[j] in uniques) {
            A = A.slice(0,j) + A.slice(j+1,A.length);
            j--;
        }
    }
    return A;
}
console.log(censor('have a nice day!!', 'av'));



function isPermu(string1, string2){
    if(string1 === string2){
      return true;
    }
    if(string1.length != string2.length){ 
      return false; 
    }
    let characters = {};
    for(let i = 0; i < string2.length ; i++ ) {
        if(string2[i] in characters) {
            characters[string2[i].toLowerCase()]++;
        } else {
            characters[string2[i].toLowerCase()]=1;
        }
    }
    string1 = string1.toLowerCase();
    for(let i = 0; i < string1.length ; i++ ) {
        let char = string1[i]
        if(!(char in characters)){
          return false;
        }else{
          characters[char]--;
        }
        if(characters[char] === 0) {
            delete characters[char];
        }
    }
    if(Object.keys(characters).length > 1){
      return false
    }
    return true;
}
 console.log(isPermu("abs","ABS"))
