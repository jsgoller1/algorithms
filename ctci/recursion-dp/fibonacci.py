import sys

def fibonacci(current, n, prev1, prev2):
    if current == n:
        return prev1 + prev2
    else:
        current += 1
        return fibonacci(current, n, prev1+prev2, prev1)


if __name__ == '__main__':
    if len(sys.argv)  != 2:
        print "Use: fibonacci.py <int>"
        sys.exit(0)
    n = int(sys.argv[1])
    if n == 0 or n == 1:
        print n
    elif n >= 998:
        print """ 
        Python's maximum recursive depth is 998; the largest recursively
        computable Fibonacci number is: 268638100244853593861467272021429
        23967616609318986952340123175997617981700247881689338369654483356
        56419182785616144335631297667364221035032463485041037768036733415
        1172899169723197082763985615764450078474174626.
        """
    else:
        print(fibonacci(0, int(sys.argv[1]), 0, 1))
