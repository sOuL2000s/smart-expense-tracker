import pandas as pd

# Sample expense data
data = {
    "Category": ["Food", "Transportation", "Entertainment", "Utilities", "Rent", "Miscellaneous"],
    "Amount": [200, 100, 150, 300, 800, 50]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate total expenses and savings tips
total_expenses = df["Amount"].sum()
print(f"Total monthly expenses: ${total_expenses}")

# Check for high expenses and suggest saving tips
if total_expenses > 1000:
    print("Your spending is high. Consider cutting down on entertainment and miscellaneous expenses.")
else:
    print("Your spending is within a reasonable range.")

# Display spending by category
print("\nSpending by category:")
print(df)
