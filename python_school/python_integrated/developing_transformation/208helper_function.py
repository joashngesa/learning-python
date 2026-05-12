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
def classify_order(item):
   
        revenue = item.get("price",0) * item.get("qty",0)
        if revenue > 500:
            return "high"
        else:
            return "low"
        
def clean_data(orders):
    clean_tbl = []
    for item in orders:
        if "price" in item and "id" in item:
            if item.get("price",0) > 0 or item.get("qty",0) > 0:
                clean_tbl.append(item)
    
    return clean_tbl

cleaned = clean_data(orders)

def transform_data(cleaned):
    transformed_tbl = []
    for item in orders:
        revenue = item.get("price",0) * item.get("qty",0)

        new_data = {
            "id":item.get("id"),
            "product": item.get("product"),
            "price": item.get("price",0),
            "quantity": item.get("qty",0),
            "revenue": revenue,
            "category": classify_order(item)
        }

        transformed_tbl.append(new_data)
        
    return transformed_tbl

transformed = transform_data(cleaned)



#using loc
def loc_transform_data(cleaned):
    return [
        {
         "id":item.get("id"),
         "product": item.get("product"),
         "price": item.get("price",0),
         "quantity": item.get("qty",0),
         "revenue": item.get("price",0) * item.get("qty",0),
         "category": classify_order(item)
        }
        for item in cleaned
    ]

loc_transformed = loc_transform_data(cleaned)



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
print("LOC transformed table: ",loc_transformed)
print("Table metrics: ",tbl_metrics)