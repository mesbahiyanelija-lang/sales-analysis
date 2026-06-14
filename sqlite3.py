import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect(r"C:\Users\mouood system\Desktop\superstore.db")
query = """
SELECT Region, SUM(Sales) as Total_Sales
FROM "superstore_final_dataset (1)"
GROUP BY Region
ORDER BY Total_Sales DESC
"""

df = pd.read_sql_query(query, conn)
print(df)

df.plot(kind="bar", x="Region", y="Total_Sales", color="steelblue")
plt.title("Sales by Region")
plt.tight_layout()
plt.show()

conn.close()
