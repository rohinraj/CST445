#Find the sum of the cosine series 1-x^2/2!+x^4/4!-x^6/6!......n terms.Use a function fact to find the factorial of the number( university question).
import math
def Series( x , n ):
    sum = 1
    term = 1
    y = 2
    for i in range(1,n):
        fct = 1
        for j in range(1,y+1):
            pass
        term = term * (-1)
        m = term * math.pow(x, y) / math.factorial(j)
        sum = sum + m
        y += 2
     
    return sum
    
x = int(input("Enter the Value of x : "))
n = int(input("Enter the Value of n : "))
print('%.4f'% Series(x, n))
