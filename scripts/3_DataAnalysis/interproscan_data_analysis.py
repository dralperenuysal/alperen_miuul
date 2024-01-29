# importing the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

print(os.getcwd())

# read the data with pandas
df = pd.read_csv("../../resource/interproscan/G_muris.tsv", sep = "\t",
                 names = list(range(0, 15)),
                 engine = "python", quoting=3)[[0, 3, 4, 5, 11, 12]]

df_ipr = df[[0, 11]]
df_ipr = df_ipr.dropna().drop_duplicates().rename(columns = {0: "id", 11: "ipr"})

#df_ipr[["ipr"]].value_counts()[:10].plot(kind="bar")
#plt.show()

# define the data will be plotting
ipr_counts = df_ipr["ipr"].value_counts()[:10]

# Plotting
plt.figure(figsize=(10, 6))  # Increase size
ax = ipr_counts.plot(kind = "bar", color = plt.cm.Paired(range(len(ipr_counts))), edgecolor='black')

# Adding labels and title with increased font size
plt.xlabel('InterPro IDs', fontsize=14)  # Adjust label as appropriate
plt.ylabel('Frequency', fontsize=14)
plt.title('Top 10 Most Frequent InterPro IDs', fontsize=16)

# Adding value labels on each bar
for index, value in enumerate(ipr_counts):
    plt.text(index, value, str(value), ha='center', va='bottom', fontsize=10)

# Improving layout
plt.xticks(rotation=45, ha='right', fontsize=12)  # Rotate x-axis labels for better readability
plt.yticks(fontsize=12)
plt.tight_layout()  # Adjusts subplot params for the subplot(s) to fit in the figure area

# Adding grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()

