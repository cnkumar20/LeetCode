package LeetCode;// This is the text editor interface.

// A) Write a changeSelector which would take in an amount and a fixed 
//  collection of coins of following denominations: 1,5,10,25  
// and output the sub-selection of coins which would total that amount. 
// The number of coins in the sub-selection should be the minimum number 
// of all such selections.
// e.g. given coin collection (2x25, 3x10, 4x5, 6x1), = 106
//       to get a change of 97 the best selection would
//       be 2x25, 3x10, 3x5, 2x1

//->can be mor than provided
//
class Coins {
    int value;
    int numberOfCoins;
    Coins(int value,int num) {
        this.value = value;
        numberOfCoins = num;
    }
    
}

class Solution {
    
    
    public boolean checkLimit(HashSet<Integer,Coins> input, int solidValue) {
        
        int total = 0;
        
        for(Integer value : input.keys()) {
            total += value * input.get(value).numberOfCoins;    
        }
        
        if(total <= solidValue) 
            return true;
        else 
            return false;
        
    }
    
    
    public HashSet<Integer,Coins> changSolver(HashSet<Integer,Coins> inputCollection, int solidValue) {

        HashSet<Integer,Coins> result = new HashSet<Integer,Coins>();
        
        // (COINSCOLLECT,97)
        //return null on fail
        
        if(checkLimit(inputCollection,solidValue))
            return null;
        
        int temp = solidValue; //97
        int count25 = 0;
        int count10 =0;
        int count5 =0;
        int count1=0;
        
        // e.g. given coin collection (2x25, 3x10, 4x5, 6x1), = 106
        //       to get a change of 97 the best selection would
        //       be 2x25, 3x10, 3x5, 2x1

        
          
            if(temp/25 >= 1) {
                if(temp/25 <= inputCollection.get(25).numberOfCoins) {
                    count25 += temp/25;
                    temp = temp%25;
                }
                else {
                    count25 = inputCollection.get(25).numberOfCoins;
                    temp = temp - inputCollection.get(25).numberOfCoins*25
                }
            }
                
            if(temp/10 >= 1) {
                if(temp/10 <= inputCollection.get(10).numberOfCoins) {
                    count10 += temp/10;
                    temp = temp%10;
                }
                else {
                    count10 = inputCollection.get(10).numberOfCoins;
                    temp = temp - inputCollection.get(10).numberOfCoins*10
                }
            }
        
        
            if(temp/5 >= 1) {
                if(temp/5 < inputCollection.get(5).numberOfCoins) {
                    count5 += temp/5;
                    temp = temp%5;
                }
                else {
                    count5 = inputCollection.get(5).numberOfCoins;
                    temp = temp - inputCollection.get(5).numberOfCoins*5
                }

            }
                
            if((temp -inputCollection.get(1).numberOfCoins) <= 0) {
                    count1 += temp;
                
            }
            else {
                return null;
            }
            
            
            result.put(25,new Coins(25,count25));
            result.put(10,new Coins(10,count10));
            result.put(5,new Coins(5,count5));
            result.put(1,new Coins(1,count1));
            
            
            return result;
        
    } 
    
}







