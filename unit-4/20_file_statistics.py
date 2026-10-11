#20 Number of characters, words and lines
with open("input.txt", "r") as f:
    data = f.read()
characters = len(data)
words = len(data.split())
lines = len(data.splitlines())
print("Characters:", characters)
print("Words:", words)
print("Lines:", lines)
