// *  Input: "ADOBECODEBANC", "ABC"
            //   b    f
//  *  Output: "BANC"
function minimumWindowSubstring(S, T) {
   let result = [0, Infinity]
   let counts = {};
   let missingCharacters = T.length;

   for(let i = 0; i < T.length; i++) { //   Create the counts hash table
     counts[T[i]] = 0;
   }
   /*
      {
        A: 0
        B: 0
        C: 0
      }
   */
   let slow = 0;

   for(let fast = 0; fast < S.length; fast++) {
     if(S[fast] in counts) { // Check if character at fast index is incounts hash
       if(counts[S[fast]] === 0) { // If you haven't seen that character before
         missingCharacters -= 1; // Decrement number of missing characters
       }
       counts[S[fast]] += 1 // And add one to its counts value
     }

     while(missingCharacters === 0) { // Shrink window until you have an incomplete set
       if((fast - slow) < (result[1] - result[0])) { //  Updates result range if smaller than previous range
         result[0] = slow;
         result[1] = fast;
       }
       //adobecodebanc
       //    b     f
       if(S[slow] in counts) {
         counts[S[slow]] -= 1
         if(counts[S[slow]] === 0) {
           missingCharacters += 1;
         }
       }
       slow += 1;
     }
   }
   return result[1] === Infinity ? "" : S.slice(result[0], result[1] + 1);
 }

console.log(minimumWindowSubstring("ADOBECODEBANC", "ABC"))