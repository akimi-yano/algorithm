import java.io.*;
import java.util.*;

class LongestCommonSubseq {
	public static void main (String[] args) {
        CommonSubSequence ans = new CommonSubSequence();
        System.out.println(ans.lcs("ABCBDAB", "BDCABA"));
	}
}
class CommonSubSequence {
	public int lcs (String A, String B) {
    int[] tab = new int[B.length()];
    int diag = 0;
    
    for(int x = 0; x < A.length();x++){
      for(int y = 0; y < B.length();y++){
        int temp = tab[y];
        if (x == 0 || y == 0){
          tab[y] = (A.charAt(x) == B.charAt(y)) ? 1 : 0;
        }
        else if (A.charAt(x) == B.charAt(y)){
          tab[y] = diag + 1;
        }
        else{
          tab[y] = Math.max(tab[y],tab[y-1]);
        }
        diag = temp;
      }
    }
		return tab[B.length() - 1];
	}
}
