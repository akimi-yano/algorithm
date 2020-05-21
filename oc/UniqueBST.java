import java.io.*;
import java.util.*;

// DO NOT EDIT
// https://leetcode.com/problems/unique-binary-search-trees/
// TreeNode class for a binary tree node
// package whatever; // don't place package name!

import java.io.*;

class MyCode {
	public static void main (String[] args) {
    UniqueTreeMem sol = new UniqueTreeMem();
		System.out.println("trees " + sol.compute(6));
    System.out.println("calls " + sol.calls);
    /*
    UniqueTreeTab sol2 = new UniqueTreeTab();
		System.out.println("trees " + sol2.trees(5));
    */
	}
}



class UniqueTreeMem {
  public int calls = 0;
  //1.cache
  Map<Integer,Integer> cache;
  public int compute(int n){
    cache = new HashMap<>();
    return tree(n);
  }
  public int tree(int n){
    //2. new basecase to cache
    if (cache.containsKey(n)) return cache.get(n);
    calls++;
    // basecase
    if (n <= 1) return 1;
    //create counter
    int counter = 0;
    //recursive case
    for(int m = 1; m <= n; m++){
      counter += tree(m - 1) * tree(n - m);
    }
    //put counter in cache
    cache.put(n,counter);
    return counter;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    }
}

class UniqueTreeTab {
  public int trees(int n){
    int tab[] = new int[n+1];
    tab[0] = 1;
    tab[1] = 1;
    for(int m = 2; m <= n; m++){
      for (int k = 1; k <= m; k++){
        tab[m] += tab[k-1] * tab[m - k];
      }
     
    }
    return tab[n];
  }
}



