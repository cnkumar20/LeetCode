package LeetCode;// This is the text editor interface.
// Anything you type or change here will be seen by the other person in real time.

import java.util.Arrays;

class BubbleSort {
    public static void sort(Integer[] input) {
        //boolean flag = true;
        for(int  i=0;i < input.length-1;i++) {
            for(int j = input.length-1; j> i ; j-- ) {
                if(input[j] < input[j-1]) {
                    int temp = input[j];
                    input[j] = input[j-1];
                    input[j-1] = temp;
                }
            }
        }
    }
    
    
    
    public static void main(String[] args) {
        //declaration
        Integer[] inputArray = {2,4,3,1,6,3,2,6,2};
        
        sort(inputArray);
        
        //print the array
        System.out.print(Arrays.deepToString(inputArray));
    }
}
