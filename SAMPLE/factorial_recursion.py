#This program defines a function called factorial that takes in a single argument, n. The function uses recursion to calculate the factorial of the input number. The base case is when n is equal to 1, in which case the function returns 1. For all other input values of n, the function returns n multiplied by the result of calling factorial(n-1). This recursive function call will continue until the base case is reached. In the example, factorial(5) is called and the output is 120.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) # prints 120

