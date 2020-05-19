
function minimumWindowSubstring(S, T) {

  let result = [0, Infinity]
  let counts = {};
  let missingCharacters = T.length;

//   Create the counts hash table
  for(let i = 0; i < T.length; i++) {
    counts[T[i]] = 0;
  }

  let slow = 0;


  for(let fast = 0; fast < S.length; fast++) {


//     Check if character at fast index is incounts hash
    if(S[fast] in counts) {
      console.log(counts)
//     If you haven't seen that character before
      if(counts[S[fast]] === 0) {

//         Decrement number of missing characters
        missingCharacters -= 1;
      }

//       And add one to its counts value
      counts[S[fast]] += 1
    }


//     Shrink window until you have an incomplete set
    while(missingCharacters === 0) {

//       Updates result range if smaller than previous range
      if((fast - slow) < (result[1] - result[0])) {
        result[0] = slow
        result[1] = fast
      }


      if(S[slow] in counts) {
        counts[S[slow]] -= 1
        if(counts[S[slow]] === 0) {
          missingCharacters += 1
        }
      }
      slow += 1;
    }
  }


  return result[1] === Infinity ? "" : S.slice(result[0], result[1] + 1);
}


console.log(minimumWindowSubstring("ADOBECODEBANC", "ABC"))