// https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
// 1520. Maximum Number of Non-Overlapping Substrings
/**
 * @param {string} s
 * @return {string[]}
 */
var maxNumOfSubstrings = function(s) {
  let intervals = [];

  let lib = {};
  let counts = {};

  // Get counts of all characters
  for (let i = 0; i < s.length; i++) {
    if (s[i] in counts) {
      counts[s[i]]++;
    } else {
      counts[s[i]] = 1;
    }
  }

  console.log("COUNTS: ", counts);

  // let alphabet = "abcdefghijklmnopqrstuvwxyz";

  // intelligently create valid intervals
  for (let char in counts) {
    let currentCount = {};

    let left = s.indexOf(char);

    let j = left;
    while (j < s.length) {
      let currentChar = s[j];
      if (currentChar in currentCount) {
        currentCount[currentChar]++;
      } else {
        currentCount[currentChar] = 1;
      }

      if (isValid(currentCount, counts)) {
        intervals.push([left, j]);
        break;
      }

      j++;
    }
  }

  console.log("INTERVALS: ", intervals);

  // sorting by end of each interval
  intervals = intervals.sort((a, b) => {
    return a[1] - b[1];
  })

  console.log("INTERVALS: ", intervals);

  let prevIntervalEnd = -1;

  let result = [];

  for (let interval of intervals) {
    if (interval[0] > prevIntervalEnd) {
      result.push(interval);
      prevIntervalEnd = interval[1];
    }
  }

  console.log("RESULT BEFORE SLICING: ", result);

  for (let i = 0; i < result.length; i++) {
    result[i] = s.slice(result[i][0], result[i][1] + 1);
  }

  return result;
};

function isValid(currentCount, counts) {
  for (let key in currentCount) {
    if (currentCount[key] < counts[key]) {
      return false;
    }
  }

  return true;
}

console.log("RESULT: ", maxNumOfSubstrings("abab"));
