#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

while True:
  amount = input()
  if amount.isalpha() == True or int(amount) <= 0:
    print("Please enter a positive integer.")
  else:
    fib = "0 1 "
    first = 0
    second = 1
    for i in range(int(amount) - 2):
      fib += str(first + second) + " "
      temp = first + second
      first = second
      second = temp
    print(fib)
    break
