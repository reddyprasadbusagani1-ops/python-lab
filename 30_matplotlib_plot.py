#30 Matplotlib scatter and line plots
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [35, 40, 45, 50, 55, 65, 70, 75, 85, 90]
}
df = pd.DataFrame(data)

plt.scatter(df["Hours"], df["Marks"])
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("Hours vs Marks")
plt.show()

plt.plot(df["Hours"], df["Marks"])
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("Hours vs Marks")
plt.show()
