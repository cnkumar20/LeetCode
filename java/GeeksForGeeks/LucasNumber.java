import java.io.*;
import java.util.*;

/*
 * To execute Java, please define "static void main" on a class
 * named Solution.
 Mathematically, Lucas Numbers may be defined as:

lucas

The Lucas numbers are in the following integer sequence:

2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123 …………..

if n = 0  L = 2
n=1 L= 1
n=2  L = 3

Lnth = L n-1th + L n-2th

Write a function int lucas(int n) n as argument and returns the n’th Lucas number.
 *
 * If you need more classes, simply define them inline.
 */

class LucasNumber {
  
  
  public static int lucasNumbers(int n) {
    if(n==0) return 2;
    if(n==1) return 1;
    
    return lucasNumbers(n-1) + lucasNumbers(n-2);
  }
  
  public static void main(String[] args) {
    System.out.println(lucasNumbers(4));
  }
}
