S = str(input("Enter The String: "))
lstWord = S.split()
lst = (sorted(lstWord,key = len))
print("Sorted Words: ")
for i in lst:
    print(i, end = " ")