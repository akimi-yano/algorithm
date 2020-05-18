function find(k = 3, n = 4, x = 2){
    let count = 0;  
    function go(length, end) {
        if (length === n) {
            if (end == x) count++;
            return;    }     
            for (let i = 1; i < k + 1; i++) {    
                 if (i != end) go(length + 1, i);    }  }  go(1, 1);  return count;} 