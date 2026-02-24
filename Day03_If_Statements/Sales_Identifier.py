sales = ["Laptop", "Mouse", "Keyboard", "Mouse", "Laptop", "Laptop", "Keyboard", "Mouse"]

sales_count = {}

for item in sales:
    if item in sales_count:
        sales_count[item] += 1
    else:
        sales_count[item] = 1

print(sales_count)

for product, count in sales_count.items():
    if count < 3:
        print("⚠️", product, "might need restock!")

for product, count in sales_count.items():
    if count > 3:
        print(product, "is a Best Seller! 🔥")
    else:
        print(product, "sold", count, "units")
