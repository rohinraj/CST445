#Write a Python program to input a list of n numbers. Calculate and display the sum of cubes of each value in the list.(university question)
lst1 = []
lst1 = [int(item) for item in input("Enter the list items seperated by Spaces : ").split()]
res = 0
for i in lst1:
    res += i*i*i
print("sum of cubes of each value in the list: "+str(res))