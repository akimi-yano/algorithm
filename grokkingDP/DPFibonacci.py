# Fibonacci
# brute force recursion solution
def calculateFibonacci(n):
  if n < 2:
    return n

  return calculateFibonacci(n - 1) + calculateFibonacci(n - 2)


def main():
  print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
  print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
  print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


main()

# top down with memorization solution
def calculateFibonacci(n):
  memoize = [-1 for x in range(n+1)]
  return calculateFibonacciRecur(memoize, n)


def calculateFibonacciRecur(memoize, n):
  if n < 2:
    return n

  # if we have already solved this subproblem, simply return the result from the cache
  if memoize[n] >= 0:
    return memoize[n]

  memoize[n] = calculateFibonacciRecur(
    memoize, n - 1) + calculateFibonacciRecur(memoize, n - 2)
  return memoize[n]


def main():
  print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
  print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
  print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


main()

# bottom up with tabulation solution
# Tabulation is the opposite of the top-down approach and avoids recursion
# In this approach, we solve the problem “bottom-up” (i.e. by solving all the related sub-problems first). 
# This is typically done by filling up an n-dimensional table. 
# Based on the results in the table, the solution to the top/original problem is then computed.
def calculateFibonacci(n):
  dp = [0, 1]
  for i in range(2, n + 1):
    dp.append(dp[i - 1] + dp[i - 2])
  return dp[n]


def main():
  print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
  print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
  print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))
main()