# LAB 4 
# SALES RECORDS
sales_data = [
    ('Marcus Webb', 'East', 4250.00),
    ('Priya Sharma', 'West', 5875.50),
    ('DeShawn Carter','East', 3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen', 'West', 4980.25)
]
total_sales = 0
# USE FOR LOOP
for name, region, sales in sales_data:
    total_sales += sales # Add to total sales 
    print(f"{name}({region}): ${sales:,.2f}") # print formatted summary

    if sales > 5000: # check top performer
        print(" ^ Top performer!")

#FINAL TOTAL 
print("\nTotal sales for all employees:", f"${total_sales:,.2f}")


