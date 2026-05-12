sales = [
    {"id": 1, "product": "Laptop", "price": 1000},
    {"id": 2, "product": "Phone", "price": -200},
    {"id": 3, "product": "Tablet"},
    {"id": 4, "product": "Monitor", "price": 300}
]
#remove invalid prices and handle missing keys
def clean_tbl(sales):
    return [item for item in sales if item.get("price",0) > 0]
    

#Ensure all data is valid
def validity_check(scrubbing):
    for item in scrubbing:
        if item.get("price",0) <= 0:
            return False
        
    return True

#calculate revenue
def calc_matrics(scrubbing):
    tbl_revenue = 0
    for item in scrubbing:
        tbl_revenue += item.get("price",0)
    return {
        "Calculated revenue": tbl_revenue,
        "Valid items": len(scrubbing)
    }


scrubbing = clean_tbl(sales)
quality_check = validity_check(scrubbing)


if quality_check:
    stats = calc_matrics(scrubbing)
    print("The pipeline is executed successfully")
    print(stats)
else:
    ("Pipeline has failed")


