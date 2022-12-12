#Remove all punctuation from a string.( use string.punctuation)
import string
S = str(input("Enter The Sentence: "))
noPunctuation = ""
for c in S:
    if c not in string.punctuation:
        noPunctuation = noPunctuation + c
print("String Without Punctuation: " + noPunctuation)