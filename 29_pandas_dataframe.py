#29 Pandas DataFrame operations
import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "Age": [20, 21, 19, 22, 20, 21, 23, 19, 22, 20],
    "Marks": [80, 75, 90, 85, 70, 88, 95, 78, 82, 91],
    "City": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "Grade": ["A", "B", "A+", "A", "B", "A", "A+", "B", "A", "A+"]
}
df = pd.DataFrame(data)
print("First 5 rows:")
print(df.head())
print("\nName column:")
print(df["Name"])
print("\nName and Marks:")
print(df[["Name", "Marks"]])
print("\nRows with Marks > 80:")
print(df[df["Marks"] > 80])
