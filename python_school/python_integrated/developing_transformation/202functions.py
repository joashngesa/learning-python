#remove negative prices
#handle missing price safely
#return cleaned list
from tabulate import tabulate

sales = [
    {"id": 1, "price": 100},
    {"id": 2, "price": -50},
    {"id": 3},  # missing price
    {"id": 4, "price": 200}
]

def clean_data(sales):
    cleaning = [item for item in sales if item.get("price",0) > 0]
    return cleaning

#ensure all prices > 0
#return True / False
def validate_data(cleaning):
    for item in cleaning:
        if item["price"] <= 0:
            return False
    
    return True

#sum all prices
#use .get()
#return total
def calc_tot_prices(cleaning):
    tot_prices = 0
    for item in cleaning:
        tot_prices += item.get("price",0)
    return tot_prices

#combine everything in a pipeline     
data_prep = clean_data(sales)
data_verification = validate_data(data_prep)
data_price_sum = calc_tot_prices(data_prep)

print(tabulate(data_prep,headers = "keys", tablefmt = "grid"))
print("Are all prices verified :",data_verification)
print("Total prices: ",data_price_sum)
    