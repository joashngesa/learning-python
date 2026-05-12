#Revenue banding
sales = [
    {"id": 1, "price": 100, "qty": 2},
    {"id": 2, "price": 400, "qty": 2},
    {"id": 3, "price": 1000, "qty": 1}
]
#create functions ; calculate_revenue(item):,classify revenue(item),transform sales(data)
#revenue > 700 → "enterprise"
#revenue > 300 → "mid_market"
#else → "small"

from tabulate import tabulate

def revenue_calc(unit):
    return unit.get("price") * unit.get("qty")

def revenue_classifier(unit):
    
        revenue = unit.get("price") * unit.get("qty")

        if revenue > 700:
            return "enterprise"
        elif revenue > 300:
            return "mid-market"
        else:
            return "small"
        
def transform_sales(sales):
    transformed_tbl = []
    for unit in sales:

        new_tbl = {
            
                "id": unit.get("id"),
                "revenue": revenue_calc(unit) ,
                "segment": revenue_classifier(unit)
            }
        
        transformed_tbl.append(new_tbl)

    return transformed_tbl

transformed = transform_sales(sales)
print(tabulate(transformed, headers = "keys", tablefmt = "grid"))