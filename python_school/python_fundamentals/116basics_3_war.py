
orders = [
    [1, "Alice", 250],
    [2, "Bob", -50],
    [3, "Charlie", 400],
    [4, "David", 0],
    [5, "Eve", 600]
]
#order pipeline
def process_orders(orders):
    cleaned_orders = [buy for buy in orders if buy[2] > 0]

#increased orders by 5%
    inc_orders = []
    order_inc_rate = 0.05
    for buy in cleaned_orders:
        new_row = [buy[0], buy[1], round(buy[2] * (1 + order_inc_rate))]
        inc_orders.append(new_row)
    
#aggregate
    tot_sales = 0
    for buy in inc_orders:
        tot_sales += buy[2]

#Orders above 300
    top_orders = [buy for buy in inc_orders if buy[2] > 300]

    return cleaned_orders, inc_orders, tot_sales, top_orders

cleaned_orders, inc_orders, tot_sales, top_orders = process_orders(orders)

print("Cleaned orders: ",cleaned_orders)
print("Orders increased: ",inc_orders)
print("Revenue: ",tot_sales)
print("Top orders: ",top_orders)
 



