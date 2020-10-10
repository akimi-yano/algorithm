/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 * 
 * https://leetcode.com/problems/greatest-common-divisor-of-strings/
 * 
 */
var gcdOfStrings = function(str1, str2) {
  let longer, shorter;
  if (str1.length > str2.length) {
    longer = str1;
    shorter = str2;
  } else {
    longer = str2;
    shorter = str1;
  }

  let divisors = [1];

  for (let i = 2; i <= shorter.length / 2; i++) {
    if (shorter.length % i === 0 && longer.length % i === 0) {
      divisors.push(i);
    }
  }

  if (longer.length % shorter.length === 0) {
    divisors.push(shorter.length)
  }

  console.log("DIVISORS: ", divisors);

  // for (let i = 0; i < divisors.length; i++) {
  //   divisors[i] = shorter.slice(0, divisors[i]);
  // }

  console.log("DIVISORS: ", divisors);

  for (let i = divisors.length - 1; i > -1; i--) {
    if (verify(longer, divisors[i], shorter) && verify(shorter, divisors[i], shorter)) {
      return shorter.slice(0, divisors[i]);
    }
  }

  return "";
};

function verify(longer, div, shorter) {
  let j = 0;
  for (let i = 0; i < longer.length; i++) {
    if (longer[i] != shorter[j]) {
      return false;
    }

    j++;
    if (j === div) {
      j = 0;
    }
  }

  if (j === 0) {
    return true;
  }
  
  return false;
}

console.log(gcdOfStrings("ABABABAB", "ABAB"))