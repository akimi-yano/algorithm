// # Given a list of words, each word consists of English lowercase letters.

// # Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere 
// #in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

// # A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a 
// # predecessor of word_2, word_2 is a predecessor of word_3, and so on.

// # Return the longest possible length of a word chain with words 
// # chosen from the given list of words.

 

// # Example 1:

// # Input: ["a","b","ba","bca","bda","bdca"]
// # Output: 4
// # Explanation: one of the longest word chain is "a","ba","bda","bdca".
 

// # Note:

// # 1 <= words.length <= 1000
// # 1 <= words[i].length <= 16
// # words[i] only consists of English lowercase letters.

// ##         dcfg         f(adcfg) = 20
// ##         dcfg         f(dcfgz) = 25
// ##    
// ## {bdca: 1, bda:2, bca:2, ba:1, b:1, a:1}
// ## bdca -> bca max(1, 1+ 1) = 2 
// ## bdca -> bda max(1, 1+1) = 2 
// ## bdca -> bdc
// class Solution:
//     def longestStrChain(self, words: List[str]) -> int:
//         longestchain = defaultdict(lambda: 1)
//         words = set(words)
//         ans = 1
//         for word in sorted(words, key=lambda e: len(e), reverse=True):
//             for i in range(len(word)):
//                 word2 = word[:i] + word[i + 1:]
//                 if word2 in words:
//                     longestchain[word2] = max(longestchain[word2], 1 + longestchain[word])
//                     ans = max(ans, longestchain[word2])
//         return ans
        
        
   
   
//    /*
   
   
   
//    /**
//  * @param {string[]} words
//  * @return {number}
//  */

function deleteIndex(word, index){
    let newWord = ''
    for(let i = 0; i <word.length; i++){
        if(i == index){
            newWord+=''
        }else {
            newWord +=word[i]
        }
    }
    
    return newWord
}

var longestStrChain = function(words) {
    words.sort((a, b)=>{return a.length - b.length})
    let map = {}
    
    for(let i = 0; i < words.length; i++){
        let word = words[i]
        if(!map[word]){
            map[word] = 1
        }
        for(let j = 0; j < word.length; j++){
            // get the index of the char of the word and delete
            let newWord = deleteIndex(word, j)
            if(map[newWord]){
                map[word] = Math.max(map[word] , 1+map[newWord])
            }
        }
    }
    
    let max = -Infinity
    for(let key in map){
        max = Math.max(max, map[key])
    }
    
    return max
}
        
console.log(longestStrChain(["a","b","ba","bca","bda","bdca"]))