package GeeksForGeeks.Arrays;

import java.io.*;
import java.util.*;
import GeeksForGeeks.DataStructure.*;

class LongestCommonSubsequence {
  
  public static int LCS(String ip1, String ip2) {
    int m = ip1.length();
    int n = ip2.length();
    
    int[][] result = new int[m+1][n+1];
    
    for(int i=0;i<=m;i++) {
     for(int j=0;j<=n;j++) {
      
       if(i==0||j==0) {
         result[i][j] = 0;
         continue; 
       }
       
       
       if(ip2.charAt(j-1) == ip1.charAt(i-1)) {
          result[i][j] = 1+ result[i-1][j-1]; 
       }
       
       else {
          result[i][j] = Math.max(result[i-1][j],result[i][j-1]); 
           
       }
     }
    }
    return result[m][n];
  }
    
  
  
  public static void main(String[] args) {
    String ip1 = "Kumar";
    String ip2 = "kuma1";
    System.out.println(LCS(ip1.toLowerCase(),ip2.toLowerCase()));
  }
}
