function root(x, n):
    if (x == 0):
        return 0

    lowerBound = 0
    upperBound = max(1, x)
    approxRoot = (upperBound + lowerBound) / 2

    while (approxRoot - lowerBound >= 0.001):
        if (power(approxRoot, n) > x):
            upperBound = approxRoot
        else if (power(approxRoot, n) < x):
            lowerBound = approxRoot
        else
            break

        approxRoot = (upperBound + lowerBound) / 2

    return approxRoot
  
  /*As we can see, the function finds an initial lower and upper bound for the answer, and sets the initial guess for the answer to be the average. Then the iteration begins, and the we notice that the following facts are true in every step of the iteration:

(approxRoot - lowerBound) = ½(upperBound - lowerBound) - Since approxRoot is always the average value between upperBound and lowerBound.
At the end of every iteration, the real root always satisfies the inequality lowerBound < root < upperBound: this is true since in the beginning of the iteration, we check if approxRoot to the power of n is greater than or lesser than x. The power function is monotonically increasing (i.e. a < b dictates that a^n < b^n) meaning this indicates whether the approximation is too high or too low.
The value of (upperBound - lowerBound) is cut by half in every iteration - since in every step we replace one of the values of upperBound or lowerBound by their current average. Obviously it means that eventually the distance between the bounds is lower than 0.001. Since the real root is between the bounds, this promises the algorithm stops.
Thus, since lowerBound< root < upperBound, then the true error - |root-approxRoot|, satisfies |root-approxRoot| < (approxRoot - lowerBound) - so it is indeed enough to check when the value on the right side is lower than 0.001.
Thus the algorithm always stops, and output of the algorithm is correct.

The best way to explain the solution algorithm is by using it on an example. Let’s try calculating the 3rd root of 7: We mark the real root as y ≅ 1.912931182772389. Our method shall iterate in a main loop, and try to produce a sequence of approximations that converge to y, until reaching a number that is close enough.

Iteration 1: Initially, we recognized that 0 < y, since 03 = 0 < 7. Also y < 7. Thus lowerBound = 0 and upperBound = 7. Our first member of the sequence is chosen to be the average between 0 and 7 - approxRoot = 3.5. Since 3.53 ≅ 42.8 > y, then we conclude that 0 < y < 3.5, so we conclude upperBound = 3.5. Note that the error is bounded: |y - approxRoot| < |3.5 - 0| = 3.5.

Iteration 2: Since we concluded that 0 < y < 3.5, our second member of the sequence should be, again, the average between our bounds 0 and 3.5 - approxRoot= 1.75. This time 1.753 ≅ 5.3 < 7, which means 1.75 < y < 3.5, so we update lowerBound = 1.75. The error is bounded by: |y - approxRoot| < |upperBound - lowerBound|= |3.5- 1.75| = 1.75. We continue the sequence this way, and notice that the error bound is reduced by half by every iteration. Here is a summary of the first few iterations in this method:

# Iteration	LowerBound	UpperBound	approxRoot value	|y- approxRoot| - True Error	Error bound
1	0	7	3.5	≅ 1.58	< 3.5 (7×2-1)
2	0	3.5	1.75	≅0.16	< 1.75 (7×2-2)
3	1.75	3.5	2.625	≅0.71	< 0.875 (7×2-3)
4	1.75	2.625	2.1875	≅0.27	< 0.4375 (7×2-4)
As we can see, by choosing the average value between By the 13th iteration, we’ll reach an error bound of 7×2^(-13), which is less than 0.001 (notice that the error may be much smaller, but since we don’t actually know the real value of y in the process of computation, we cannot promise a better bound).

Time Complexity: notice that every loop iteration is done in O(1), under the assumption that the power function takes a constant time. The initial error is x, and the error is multiplied by 0.5 in every iteration. Thus the number of iterations is the minimal k such that: 2^(-k) x<0.001 i.e. 2^(-k)<(0.001 / x) k >log(x) + 3log(10) = O(log(x)) The number of iterations is therefore O(log(x)), meaning the total runtime is O(log(x)) if we refer to the value stored in x, or O(x) if we refer to the number of bits required to represent x (since it takes Log(x) in average bits to represent a number x).

Space Complexity: O(1), since we only need a constant number of variables for the algorithm.

Mathematical Note: our explanation used the fact that power function x^n is a monotonically increasing continuous function on the positive numbers. Although it is true, the Intermediate value theorem in calculus, states that this method will work for every continuous function - but the proof for this requires more mathematical tools.*/
