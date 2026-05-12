#COMBINED HELPER STYLE
orders = [
    {"id": 1, "price": 150, "qty": 2},
    {"id": 2, "price": 50, "qty": 1},
    {"id": 3, "price": 500, "qty": 3}
]

#Build functions that calculate: revenue,classify order,transform orders, metrics
#Rules; revenue > 1000 → "high"
#       revenue > 200 → "medium"
#       else → "low"
#metrics;total revenue and total orders

from tabulate import tabulate

def revenue_calc(item):
    return item.get("price") * item.get("qty")

def order_classifier(item):
    revenue = revenue_calc(item)

    if revenue > 1000:
        return "high"
    elif revenue > 200:
        return "medium"
    else:
        return "low"
    

def transform_orders(orders):
    return [
        {
            "id": item.get("id"),
            "price": item.get("price"),
            "quantity": item.get("qty"),
            "revenue": revenue_calc(item),
            "class": order_classifier(item)
        }
        for item in orders
    ]

transformed = transform_orders(orders)

def calc_metrics(transformed):
    total_orders = 0
    for item in transformed:
        total_orders += item.get("quantity")

    total_revenue = 0
    for item in transformed:
        total_revenue += item.get("revenue")

    return {
        "Total_orders": len(transformed),
        "Total_revenue": total_revenue
    }

order_metrics = calc_metrics(transformed)

print(tabulate(transformed, headers = "keys", tablefmt = "grid"))
print("Order metrics: ",order_metrics)