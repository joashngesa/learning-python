#Discount classification

orders = [
    {"id": 1, "price": 1000, "qty": 1},
    {"id": 2, "price": 200, "qty": 2},
    {"id": 3, "price": 50, "qty": 10}
]

#create helper function
#revenue > 800 → "premium"
#revenue > 300 → "standard"
#else → "basic"

def discount_classifier(item):
   
        revenue = item.get("price",0) * item.get("qty",0)

        if revenue > 800:
            return "premium"
        elif revenue > 300:
            return "standard"
        else:
            return "basic"
        

def transform_data(orders):

    return [
        {
            "id": item.get("id"),
            "revenue": item.get("price",0) * item.get("qty",0),
            "category": discount_classifier(item),
        }
        for item in orders
    ]

transformed = transform_data(orders)
print("transform data: ",transformed)