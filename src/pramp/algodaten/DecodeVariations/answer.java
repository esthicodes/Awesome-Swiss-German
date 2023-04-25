import java.io.*;
import java.util.*;

class Solution {

	static int decodeVariations(String S) {
    int[] dp = new int[S.length() + 1];
    dp[0] = 1;
    if (S.charAt(0) != '0'){
      dp[1] = 1;
    } else {
      dp[1] = 0;
    }
    for (int i = 2; i <= S.length(); i++){
      
      int oneD = Integer.parseInt(S.substring(i-1, i));
      int twoD = Integer.parseInt(S.substring(i-2, i));
      
      if ( 1 <= oneD && oneD <= 9){
        dp[i] += dp[i-1];
      }
      if ( 10 <= twoD && twoD <= 26){
        dp[i] += dp[i-2];
      }
    }
    return dp[S.length()];
	}

	public static void main(String[] args) {
    
	  System.out.println(decodeVariations("1262") + " Should be 3");
    
	}
}

