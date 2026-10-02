 TASK 2 - DATA VISUALIZATION

data = {
    "Technology": [45000, 12000],
    "Furniture": [33000, 7500],
    "Office Supplies": [25500, 8500]
}

print("DATA VISUALIZATION REPORT")
print("-------------------------")

total_sales = 0
total_profit = 0

for category, values in data.items():
    sales = values[0]
    profit = values[1]

    print(category)
    print("Sales :", sales)
    print("Profit:", profit)
    print()

    total_sales += sales
    total_profit += profit

print("-------------------------")
print("Total Sales :", total_sales)
print("Total Profit:", total_profit)

print("\nKEY INSIGHTS")
print("1. Technology has the highest sales.")
print("2. Furniture has medium sales.")
print("3. Office Supplies has lower sales.")
print("4. Technology has the highest profit.")

print("\nTask 2 completed successfully!")