# Item Cost
num = float(input("Enter a Purchase Price: "))

# loyality Points
num_2 = float(input("Enter Loyality Points: "))

# Veteran Discount
vet_disc = float(num * .10)

# Taxes to be collected
weed_tax_1 = float(num * .0789)
weed_tax_2 = float(num * .0705)
weed_tax_3 = float(num * .04)

# Calculations
result_1 = num - vet_disc
result_2 = result_1 + weed_tax_1
tax_total = weed_tax_1 + weed_tax_2 + weed_tax_3
total = result_1 + weed_tax_1 + weed_tax_2 + weed_tax_3 - num_2
total_2 = weed_tax_1 + weed_tax_2 + weed_tax_3 + num

# Totals on Displays
print("Veteran Discount = ","$", vet_disc)
print("Illinois Rec Tax = ","$", weed_tax_1)
print("Rec Cannabis Tax = ","$", weed_tax_2 + weed_tax_3)
print("Total taxes collected = ","$", tax_total)
print("Total without discounts", "$", total_2 )
print("Total with discounts = ","$", total)