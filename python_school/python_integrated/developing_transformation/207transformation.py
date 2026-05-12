orders = [
    {"id": 1, "product": "Laptop", "price": 1000, "qty": 1},
    {"id": 2, "product": "Mouse", "price": 50, "qty": 5},
    {"id": 3, "product": "Keyboard", "price": 80},
    {"id": 4, "product": "Monitor", "price": 300, "qty": 2}
]
#printing after function was done only for computation and learning sake to check the output at each stage
#must have "price"
#must have "qty"
#price > 0
#qty > 0
#clean data
def clean_data(orders):
    cleaned_tbl = []
    for item in orders:
        if "price" in item and "qty" in item: 
            if item.get("price",0) > 0 and item.get("qty",0) > 0:
                cleaned_tbl.append(item)

    return cleaned_tbl

            

cleaned = clean_data(orders)
print("Cleaned table: ",cleaned)

#keep "id" and "product"
#create:
#"revenue" = price * qty
#"category":
#"high" if revenue > 500
#"low" otherwise

def transform_data(cleaned):
    processed_tbl = []

    for item in cleaned: 
        revenue = item.get("price",0) * item.get("qty",0)

        if revenue > 500:
            category = "high"
        else:
            category = "low"

        new_record = {
            "id":item.get("id"),
            "product":item.get("product"),
            "revenue":revenue,
            "category":category
        }

        processed_tbl.append(new_record)

    return processed_tbl

processed = transform_data(cleaned)

print("Processed table: ",processed)

def transform_table(cleaned):
    return [
        {
            "id": item.get("id"),
            "product": item.get("product"),
            "price": item.get("price",0),
            "qty": item.get("qty",0),
            "revenue": item.get("price",0) * item.get("qty",0),
            "category": "high" if item.get("price",0) * item.get("qty",0) > 500 else "low" 
        }
        for item in cleaned
    ]

transformed = transform_table(cleaned)


#calculate metrics; total orders,total revenues
def calc_metrics(transformed):
    
    tot_revenue = 0
    for item in transformed:
        tot_revenue += item.get("revenue",0)

    return {
        "total orders":len(transformed),
        "total revenue":tot_revenue
    }

tbl_metrics = calc_metrics(transformed)
print("Transformed table: ",transformed)
print("Table metrics: ",tbl_metrics)