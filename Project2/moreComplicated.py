# Parth Parth and Chandrachud Malali Gowda
# Python Fibonacci Term Calculator
# CS333 Project 2
# 2/24/2022

def main():
  # get input from user
  n = int(input("Enter the fibonacci term needed: "))
  # call fibonacci function
  print(fibonacci(n))

def fibonacci(n):
  if n < 0:
    return "Error: negative number"
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
  main()