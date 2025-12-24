import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/shipments_q2_2025.csv")

# Plot
plt.figure(figsize=(10,6))
plt.bar(df["Company"], df["Shipments_Million"], color=['#0A0AFF','#A2AAAD','#FF5733','#33FF57','#FF33A6'])
plt.title("Top 5 Mobile Companies by Global Smartphone Shipments (Q2 2025)")
plt.xlabel("Company")
plt.ylabel("Shipments (Million Units)")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save chart
plt.savefig("charts/top5_mobile_sales_q2_2025.jpeg", dpi=300)
plt.show()

