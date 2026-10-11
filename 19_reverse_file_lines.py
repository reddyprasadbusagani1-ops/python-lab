#19 Print each line of file in reverse order
with open("input.txt", "r") as f:
    for line in f:
        print(line.rstrip()[::-1])
