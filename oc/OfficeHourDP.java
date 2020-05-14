// package whatever; // don't place package name!

import java.io.*;
import java.util.*;

class MyCode {
	public static void main (String[] args) {
    GenerateArrayM sol = new GenerateArrayM();
		System.out.println(sol.compute(4,3,2));
    GenerateArrayT sol2 = new GenerateArrayT();
		System.out.println(sol2.GA(4,3,2));
	}
}
//memoization:
class GenerateArrayM {
  int n;
  int k;
  int x;
  //1. make and intiliaze cache
  public Map<String,Integer> cache = new HashMap<>();
  public int compute(int n,int k, int x){
    this.n = n;
    this.k = k;
    this.x = x;
    return GA(n-1,true);
  }
  public int GA(int i, boolean v){
    //make string key to represent current subproblem
    String key = i + "_" + v;
    //base cases:
    //2. add cache check to base cases
    if (cache.containsKey(key)) return cache.get(key);
    //base cases for [1]
    if (i == 0){
      if (v) return 0;
      else return 1;
    }
    //recursive cases:
    //3. create counter
    int counter = 0;
    if (v){
      //normal recursive case: return GA(i-1,F);
      counter += GA(i-1,false);
    }else{
      //normal recursive case: return GA(i-1,T)*(k-1) + GA(i-1,F)*(k-2);
      counter += GA(i-1,true)*(k-1) + GA(i-1,false)*(k-2);
    }
    //put current subproblem in cache
    cache.put(key,counter);
    return counter;
  }
}
//tabulation
class GenerateArrayT {
  public int GA(int n,int k, int x){
    int[][] tab = new int[n][2];
    //these are for our base case with a 
    //change to represent an edge case
    //if x is 1 then a list of length 1 that ends in x is possible
    //and a list of length 1 that doesnt end in x is not possible
    tab[0][0] = x == 1 ? 1 : 0;
    tab[0][1] = x != 1 ? 1 : 0;
    for(int i = 1; i < n; i++){
        tab[i][0] = tab[i-1][1];
        tab[i][1] = ((tab[i-1][0] * (k-1)) + (tab[i-1][1] *(k-2))) % 1000000007;
    }
    return tab[n - 1][0];
  }
}
