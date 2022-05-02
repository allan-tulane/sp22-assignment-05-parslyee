# CMPS 2200 Assignment 5
## Answers

**Name:**Lily Yee


Place all written answers from `assignment-05.md` here for easier grading.



- **1a.**

In order to do this, we first need to find a coin with the largest value less than N. Since the coins are worth 2^k, we can use an algorithm that will find the combination with the fewest amount of coins that sum to N. Regarding possible base cases, if N = 0, then the algorithm returns O. If N = 1, then the algorithm returns 2^0. Moving past the base case, the algorithm would first find the greatest possible 2^k less than N and subtract it from N. Then, the algorithm would find the next greatest possible 2^k less than the new N, and continue this process, adding each version of 2^k to a total sum until N = 1 or 0. 

- **1a.** 

This algorithm has work of W(n) = W(N) + 1 and span of S(n) = S(N) + 1 because it is sequential and dependent on the size of N. There is also an additional cost of adding each coin to a total sum. 

- **2a.**

One counter example could involve the denominations = {1, 5, 7, 13, 14} and N = 20. A greedy algorithm would select 14, 5, and 1, returning 3 coins. An optimal solution would be to select 7 and 13, and return 2 coins. 


- **2b.**

If we used dynamic programming rather than a greedy algorithm, we could use a bottom-up approach to better solve the problem. We can find all of the possible combinations that sum to N and then select the optimal solution. We can store the combinations in a dictionary that has the value of each coin and the total number of coins used, selecting the dictionary entry with the minimum second value. 

The work would be W(N) = W(N * coins) and span would be S(N) = S(N). 

- **3a.**

The optimal substructure property for this version of the edit distance problem and modified MED is :

{MED(S[1:], T[1:]), if S[0] = T[0]. When S[0] != T[0], then 1+min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:],T[1:])). 


