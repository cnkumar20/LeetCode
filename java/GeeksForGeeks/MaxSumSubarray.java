import java.io.*;
import java.util.*;

/*
 * To execute Java, please define "static void main" on a class
 * named Solution.
 *
 * If you need more classes, simply define them inline.
 */

class MaxSumSubarray {
  
  public static int maxSubArray(int[] input) {
      int curMax =0;
      int maxSum = 0;
    
      for(int i=0;i<input.length;i++) {
        curMax += input[i];
        
        if(curMax < 0) {
          curMax = 0; 
        }
        
        maxSum = maxSum < curMax ? curMax:maxSum;
        
      }
    
      return maxSum;
    
  }
  
  
  public static void main(String[] args) {
    int[] input = {1,2,-1,-2,4,2,-3,1,-1};
    
    System.out.println(maxSubArray(input));
  }
}
