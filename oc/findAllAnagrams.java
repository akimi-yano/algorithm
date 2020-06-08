// https://leetcode.com/problems/find-all-anagrams-in-a-string/

import java.io.*;
import java.util.*;

class findAllAnagrams {
	public static void main (String[] args) {
    Solution sol = new Solution();
		System.out.println(sol.findAnagrams("cbacbabacd","abc"));
	}
}
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> out = new ArrayList<>();
        int[] window = new int[26];
        int[] pattern = new int[26];
        for(int i = 0; i < p.length(); i++){
          char cs = s.charAt(i);
          window[cs - 'a']++;
          char cp = p.charAt(i);
          pattern[cp - 'a']++;
        }

        if (Arrays.equals(window,pattern)) out.add(0);
        for(int r = p.length(); r < s.length(); r++){
          int right = s.charAt(r) - 'a';
          int left = s.charAt(r - p.length()) - 'a';
          window[right]++;
          window[left]--;
          if (Arrays.equals(window,pattern)) out.add(r - p.length() + 1);  
        }
        
        return out;
    }
}