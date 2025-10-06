#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
while True:
    user_input = input("Enter the amount of terms of the Fibonacci sequence you want?")

    while user_input.isdigit() == False or int(user_input) <= 0:
        print("Please enter a positive integer.")
        user_input = input("Enter the amount of terms of the Fibonacci sequence you want?")

    user_input = int(user_input)

    a, b = 0, 1
    for i in range(user_input):
        print(a, end=" ")
        next_term = a + b
        a = b
        b = next_term
