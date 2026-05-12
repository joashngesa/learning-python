
#clean_data(data)
sales = [
    [101, "Laptop", 1000],
    [102, "Phone", -200],
    [103, "Tablet", 500],
    [104, "Monitor", -100],
    [105, "Keyboard", 80]
]
def cleaning_data(sales):
    cleaned_data = [txn for txn in sales if txn[2] > 0]
    return cleaned_data

#transform_data(data)-increased prices by 10%
def increasing_prices(cleaned_data):
    inc_prices = []
    price_increase_rate = 0.10
    for txn in cleaned_data:
        new_row = [txn[0], txn[1], round(txn[2] * (1 + price_increase_rate))]
        inc_prices.append(new_row)
    return inc_prices

#calculate_total(data)
def total_data(inc_prices):
    totals = 0
    for txn in inc_prices:
        totals += txn[2]
    return totals

#high_value(data) > 600
def high_value(inc_prices):
    over_600 = [txn for txn in inc_prices if txn[2] > 600]
    return over_600

cleaned = cleaning_data(sales)
adjusted = increasing_prices(cleaned)
revenue = total_data(adjusted)
top_value = high_value(adjusted)

print("Cleaned data: ",cleaned)
print("Increased prices: ",adjusted)
print("Revenue: ",revenue)
print("Top products: ",top_value)


