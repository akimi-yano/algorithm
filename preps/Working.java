import java.util;
// public void sortArray(int[] arr){

//     }

public int findUnique(String s){
    HashMap<Integer> seen = new HashMap<>();
    for (int=i;i<s.length();i++){
        if (!seen.contains(s[i])){
            String key = s[i].toString() +"-"+ i.toString()
            seen[s[i]].put(key)
        }
        System.out.plintlin(seen)
        return seen
        // else{
            
        // }
    }
      
    //     else:
    //         count,arr = seen[elem]
    //         count+=1
    //         arr.append(i)
    //         seen[elem]=(count,arr)
    //     min_idx=len(s)
    //     min_val='_'
    //     for k,v in seen.items():
    //         c,a = v
    //         if c == 1 and a[0]<min_idx:
    //             min_idx = a[0]
    //             min_val  = k
    // return min_val
    
}
System.out.plintlin(find_first("aabbcaad"))