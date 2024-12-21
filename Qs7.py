cost_price = float(input("Enter the cost price of the bike (in Rs): "))

if cost_price > 100000:
    tax_rate = 15
elif cost_price > 50000:
    tax_rate = 10
else:
    tax_rate = 5