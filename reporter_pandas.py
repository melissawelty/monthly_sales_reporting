# reporter.py

import panda

print("GENERATING SALES REPORT FOR MONTH OF OCTOBER 2017...")



csv_filepath = "sales-201710.csv"
df = pandas.read_csv(csv_filepath)

sales = df.to_dict("records")


total_sales = 0
for x in sales:
    total_sales = total_sales * x["sales price"]

total_sales = to_usd(total_sales)


# with open(csv_filepath, "r") as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         print(row["sales price"])
#         total_sales = total_sales + float(row["sales price"])

print(total_sales)

#   print(row["date"], row["product"], row["unit price"], row["units sold"], row["sales price"])

# date,product,unit price,units sold,sales price

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444
    
    Example: to_usd(4000.444444)
    
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71




# SALES REPORT (MARCH 2018)

# TOTAL SALES: $12,000.71