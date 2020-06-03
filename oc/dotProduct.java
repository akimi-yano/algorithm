// package whatever; // don't place package name!

import java.io.*;
import java.util.*;

class dotProduct{
	public static void main (String[] args) {
    DotProductMem sol1 = new DotProductMem();
    DotProductTab sol2 = new DotProductTab();
    int[] nums1 = new int[]{2,1,-2,5};
    int[] nums2 = new int[]{3,0,-6};
    System.out.println(sol1.compute(nums1,nums2));
    System.out.println(sol1.calls + '\n');
    
    //System.out.println(sol2.dotprod(nums1,nums2));
    
	}
  
}
class DotProductMem {
  //1.cache
  Map<String,Integer> cache;
  int calls;
  int[] n1;
  int[] n2;
  public int compute (int[] nums1, int[] nums2){
    //intialize cache
    cache = new HashMap<>();
    n1 = nums1;
    n2 = nums2;
    return dotprod(nums1.length - 1,nums2.length - 1);
  }
  public int dotprod(int i, int j){
    String key = i + "_" + j;
    int prod = n1[i] * n2[j];
    //basecase
    //2.check if in cache
    if (cache.containsKey(key)) return cache.get(key);
    if (i == 0 && j == 0) return prod;
    calls++;
    //recursive
    //3. create counter
    int counter = 0;
    if (i == 0){
      counter += Math.max(prod,dotprod(i,j - 1));
    }
    else if (j == 0) {
      counter += Math.max(prod,dotprod(i - 1, j));
    }
    else{
      calls += 2;
      counter += Math.max(dotprod(i - 1,j - 1) + Math.max(prod,0),
          Math.max(prod,Math.max(dotprod(i-1,j),dotprod(i,j-1))));
    }
    //4.put in cache
    cache.put(key,counter);
    return counter;
    
    
  }
}
class DotProductTab {
    public int dotprod(int[] nums1, int[] nums2) {
        int[][] dp = new int[nums1.length][nums2.length];
        for(int i = 0; i < nums1.length; i++){
            for(int j = 0; j < nums2.length; j++){
                int p = nums1[i]*nums2[j];
                if ((i == 0) && (j == 0)){
                    dp[i][j] = p;
                }
                else if (i == 0) {
                    dp[i][j] = Math.max(p,dp[i][j-1]);
                }else if (j == 0){
                    dp[i][j] = Math.max(p,dp[i-1][j]);
                }else{
                    dp[i][j] = Math.max(dp[i-1][j-1] + Math.max(p,0),Math.max(p,Math.max(dp[i-1][j],dp[i][j-1])));
                }
            }
        }
        for (int[] r : dp){
          System.out.println(Arrays.toString(r));
        }
        return dp[nums1.length - 1][nums2.length - 1];
    }                                                                           
}
