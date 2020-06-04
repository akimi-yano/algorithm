// # 7. Reverse Integer

// # Given a 32-bit signed integer, reverse digits of an integer.

// # Example 1:

// # Input: 123
// # Output: 321
// # Example 2:

// # Input: -123
// # Output: -321
// # Example 3:

// # Input: 120
// # Output: 21
// # Note:
// # Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
// # For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

// package whatever; // don't place package name!
/*
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

devide with 10 and and add the value of module of 10


Note:
Assume we are dealing with an environment which could only 
store integers within the 32-bit signed integer range: 
[−231,  231 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.
*/

import java.io.*;

class MyCode {
	public static void main (String[] args) {
		System.out.println(reverse(2147483648));
	}
  public  static int reverse(int num) {
    int res = 0;
    boolean isNegative = num < 0;
    if(isNegative) {
      num *= -1;
    }
    while(num > 0) {
      if(res > Integer.MAX_VALUE / 10) return 0;
      res = (res * 10) + (num % 10);   
      num /= 10;
    }
    return isNegative ? res * -1 : res;
  }
}

// pop = num % 10

// 2 ^31 = 2147483648
// (rev > Integer.MAX_VALUE/10 || 
// (rev == Integer.MAX_VALUE / 10 && pop > 7)) return 0;

// largest no. 2147483647
// original 7463847....