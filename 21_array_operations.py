#21 Array operations
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input("Enter element: ")))
print("Array:", arr)
value = int(input("Enter element to append: "))
arr.append(value)
print("After append:", arr)
value = int(input("Enter element to insert: "))
pos = int(input("Enter position: "))
arr.insert(pos, value)
print("After insertion:", arr)
arr.reverse()
print("After reverse:", arr)
