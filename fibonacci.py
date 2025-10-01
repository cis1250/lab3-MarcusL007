#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

while True:
  amount = input()
  if amount.isDigit() == False or amount <= 0 or isinstance(amount, int) == False:
    continue
  else:
    first = 0
    second = 1
    print(first)
    print(second)
    for i in range(int(amount) - 2):
      print(first + second)
      temp = first + second
      first = second
      second = temp
