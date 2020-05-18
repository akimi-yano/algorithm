
import java.io.*;
import java.util.*;


class DPCoinSum {
	public static void main (String[] args) {
    LatticePaths solution = new LatticePaths();
		System.out.println("Number of Paths: " + solution.compute(10,10));
    System.out.println("Number of recursive calls: "+ solution.calls);
    CoinSumMem solution2 = new CoinSumMem();
    System.out.println("Number of combinations: " + solution2.compute(5,new int[]{1,2,4}));
    System.out.println("Number of recursive calls: "+ solution2.calls);
    CoinSumTab solution3 = new CoinSumTab();
    System.out.println("Number of combinations: " + solution3.cs(5,new int[]{1,2,4}));
	}
  
}
class LatticePaths{
  public int calls = 0;
  Map<String,Integer> cache;
  public int compute(int m,int n){
    cache = new HashMap<>();
    return lp(m,n);
  }
  public int lp(int m, int n){
    String key = m + "_" + n;
    //basecases
    if (cache.containsKey(key)) return cache.get(key);
    if (m == 0 && n == 0) {
      return 1;
    }
    if (m < 0 || n < 0) {
      return 0;
    }
    calls++;
    //recursive case
    int counter = lp(m-1,n) + lp(m,n-1);
    cache.put(key,counter);
    return counter;
  }
}
class CoinSumMem{
  public int calls = 0;
  public int coins[];
  Map<String,Integer> cache;
  public int compute(int target,int[] coins){
    cache = new HashMap<>();
    this.coins = coins;
    return cs(target, coins.length - 1);
  }
  public int cs(int target, int coin){
    //base case:
    String key = target + "_" + coin;
    if (cache.containsKey(key)) return cache.get(key);
    //target 0 coin 0
    if (target == 0 && coin == -1) return 1;
    //target < 0
    if (target < 0) return 0;
    
    //coins is 0 target not 0
    if (coin == -1) return 0;
    
    //recursive cases
    //use coin and subtract from target
    calls++;
    int counter = cs(target-coins[coin], coin) + cs(target, coin -1);
    //dont use coin keep target the same
    cache.put(key,counter);
    return counter;
  }
}
class CoinSumTab{
  public int cs(int target, int[] coins){
    int[] tab = new int[target +1];
    tab[0] = 1;
    for (int c = 0; c < coins.length; c++){
        int curCoin = coins[c];
      for (int tabIndex = 0; tabIndex <= target; tabIndex++){
        if (tabIndex - curCoin >= 0) tab[tabIndex] += tab[tabIndex - curCoin];
        System.out.println(Arrays.toString(tab));
      }
      System.out.println("\n");
    }
    return tab[target];
  }

  public void print(int[][] tab){
    for(int[] row : tab){
      System.out.println(Arrays.toString(row));
    }
    System.lineSeparator();
  }
}

