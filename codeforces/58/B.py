"""
#1 brute force / knapsack?
- get all divisors of n
- for each divisor:
    - get max value of count for each prev divisor dividing it as well
    - store best one as prev and its count plus 1
- walk backwards from n, printing 

(can also likely be solved recursively by solving for cases less than n
that must be divisible by n)
------
#2  get all divisors and solve as a knapsack problem?
- find all divisors from 1 to n
- for each divisor, see what max is if we include it or not

trying to find denomination with most coins
most coins for including c_i = max(most for c_(i-1), most for most recent divsor of c_i + 1)
-------------------
#3 Also can be a graph search:
- build adjacency list: j has directed edge to k if k | j; 100 has directed edge to 50 because 50 | 100.
    - get all divisors from 1 to n of n
    - each time a divisor k of n is found, add edge from n to k, and add edges from k to any previous divisors of n that are also divisors of k
- find longest path in graph from n to 1. Shortest path can be achieved with BFS. Since all edges are equal weight, we could exhaustively explore the graph and keep track of longest graph. 
    - Could leverage caching? do we need to re-explore routes if we already know the longest way to get to 1 from them? 
        - Won't be too helpful, will be very small graph since there are likely fewer than 100 nodes, each of which will have relatively few edges
"""

def solve_case_dp(n):
    """
    Approach #2
    """
    # (i, max coins, prev coin)
    divisors = [(1, 1, None)]
    for i in range(2, n+1):
        if (n % i == 0):
            divisors.append((i, 1, None))
    
    for i, divisor in enumerate(divisors[1:], start=1):
        curr = divisor[0]
        for j, j_max, j_prev in divisors[i-1::-1]:
            if (curr % j  == 0) and (j_max >= divisors[i][1]):
                divisors[i] = (curr, j_max+1, j)      
    
    curr = n
    for i, _, prev in divisors[::-1]:
        if i == curr:
            print(i, end=" ")
            curr = prev


def solve_case(n):
    """
    According to the editorial, we apparently can also use a greedy approach.
    """
    divs = []
    prev = 1
    for i in range(1, n+1):
        if (i%prev==0) and (n%i==0):
            divs.append(i)
            prev = i
    for div in divs[::-1]:
        print(div, end=" ")

if __name__ == '__main__':
    i = int(input())
    solve_case(i)
    #print("")
    #solve_case_dp(i)
