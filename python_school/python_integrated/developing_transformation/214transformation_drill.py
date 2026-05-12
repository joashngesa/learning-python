#WAREHOUSE STOCK SIGNAL
stock = [
    {"sku": "X1", "units": 5},
    {"sku": "X2", "units": 20},
    {"sku": "X3", "units": 100}
]

#Create function that gives stock signal and transform stock
#units < 10 → "reorder_now"
#units < 50 → "watch"
#else → "healthy"

from tabulate import tabulate 

def stock_signal(piece):
    if piece.get("units") < 10:
        return "reorder_now"
    elif piece.get("units") < 50:
        return "watch"
    else:
        return "healthy"
    
def transform_stock(stock):
    stock_tbl = []
    for piece in stock:
        cat_stock = {
                "sku": piece.get("sku"),
                "units": piece.get("units"),
                "signal": stock_signal(piece)
            }
        
        stock_tbl.append(cat_stock)
    
    return stock_tbl

transformed = transform_stock(stock)
print(tabulate(transformed, headers = "keys", tablefmt = "grid"))
    