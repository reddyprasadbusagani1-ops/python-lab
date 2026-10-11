#15 Check key exists in dictionary
d = {
    "name": "Ravi",
    "age": 20,
    "city": "Hyderabad"
}
key = input("Enter key: ")
if key in d:
    print("Key exists")
else:
    print("Key does not exist")
