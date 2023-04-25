import java.io.*;
import java.util.*;

class Solution {

  static double root(double x, int n) {
    
   double output=1;
    
    while(Math.pow(output, n) < x ) {
      output++;
    }
    
    if(Math.pow(output, n) == x) {
      return output;
    }
    
    double start = output-1;
    
    double result = 1;
    
    for(double i=start; i < output; i += 0.01) {
      result = Math.pow(i, n);
      
      if(result == x) {
        output = i;
        break;
      }
      if(result > x) {
        output = i-0.01;
        break;
      }
    }
    return output;
  }

  public static void main(String[] args) {

  }

}

// https://github.com/esthicodes
