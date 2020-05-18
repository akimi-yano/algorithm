/**
 * @param {string[]} pizza
 * @param {number} k
 * @return {number}
 */
var ways = function(pizza, k) {
  
  const preProcess = [];
  for (let i = 0; i < pizza.length; i++) {
    preProcess.push([]);
    
    for (let j = 0; j < pizza[0].length; j++) {
      preProcess[i].push(0);
    }
  }
  
  preProcess[preProcess.length - 1][preProcess[0].length - 1] = (pizza[pizza.length - 1][pizza[0].length - 1] === "A") ? 1 : 0;
  
  // right most column
  
  for (let y = pizza.length - 2; y >= 0; y--) {
    if (pizza[y][pizza[0].length - 1] === "A") {
      preProcess[y][pizza[0].length - 1] = preProcess[y + 1][pizza[0].length - 1] + 1;
    } else {
      preProcess[y][pizza[0].length - 1] = preProcess[y + 1][pizza[0].length - 1];      
    }
  }
  
  // bottom row
  
  for (let x = pizza[0].length - 2; x >= 0; x--) {
    if (pizza[pizza.length - 1][x] === "A") {
      preProcess[pizza.length - 1][x] = preProcess[pizza.length - 1][x + 1] + 1;
    } else {
      preProcess[pizza.length - 1][x] = preProcess[pizza.length - 1][x + 1];      
    }
  }
  
  // rest of pre processing
  
  for (let y = pizza.length - 2; y >= 0; y--) {
    for (let x = pizza[0].length - 2; x >= 0; x--) {
      preProcess[y][x] = (pizza[y][x] === 'A') ? 1 : 0;
      
      preProcess[y][x] = preProcess[y][x + 1] + preProcess[y+1][x] - preProcess[y+1][x+1] + preProcess[y][x];
    }
  }
  
  
  const cache = {};
  function findWays(xTL, yTL, xBR, yBR, k, prevCount) {
    let key = xTL + '_' + yTL + '_' + xBR + '_' + yBR + '_' + k + '_' + prevCount;
    
    if (key in cache) {
      return cache[key];
    }
    let currentCount = preProcess[yTL][xTL];
    
    if (currentCount < k) {
      return 0;
    }
    if (prevCount === currentCount) {
      return 0;
    }
    if (k === 1 && currentCount >= 1) {
      return 1;
    }
    
    let ways = 0;
    
    // vertical cuts
    for (let x = xTL + 1; x <= xBR; x++) {
      ways += findWays(x, yTL, xBR, yBR, k - 1, currentCount);
    }
    
    // horizontal cuts
    for (let y = yTL + 1; y <= yBR; y++) {
      ways += findWays(xTL, y, xBR, yBR, k - 1, currentCount);
    }
    
    // vertical cuts second half

    // horizontal cuts second half
    
    cache[key] = ways;
    return ways;
  }
  
  let result = findWays(0, 0, pizza[0].length - 1, pizza.length - 1, k, Infinity);
  return result % (1000000000 + 7)
};


console.log(ways(["A..","AAA","..."], 3));
