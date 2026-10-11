#14 Count vowels without control flow
s = input("Enter a string: ")
count = sum(map(s.lower().count, "aeiou"))
print("Number of vowels:", count)
