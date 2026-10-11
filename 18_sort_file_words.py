#18 Sort words from one file into another
with open("input.txt", "r") as f:
    words = f.read().lower().split()
words.sort()
with open("output.txt", "w") as f:
    for word in words:
        f.write(word + "\n")
print("Words sorted successfully.")
