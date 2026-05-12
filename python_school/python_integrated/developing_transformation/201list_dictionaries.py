
sales = [
    {"id": 1, "product": "Laptop", "price": 1000},
    {"id": 2, "product": "Phone", "price": -200},
    {"id": 3, "product": "Tablet", "price": 500}
]

#print only valid records (price > 0)_assumption is the q is asking for only valid records
for product in sales:
    if int(product["price"]):
        product
    elif product["price"] > 0:
        product
    else:
        None
#LOC -Print only valid records (price > 0)
validated_sales = [product for product in sales if product["price"] > 0]
print(validated_sales)

#count valid items
valid_count = 0
for product in sales:
    valid_count += 1
print(valid_count)

#total revenue
revenue = 0
for product in sales:
    if product["price"] > 0:
        revenue += product["price"]
print(revenue)

#total revenue
revenue2 = sum([product["price"] for product in sales])

# build a function that only returns valid sales
def sales_validation(sales):
    cleaned_sales = []
    for product in sales:
        if product["price"] > 0:
            cleaned_sales.append(product)
    return cleaned_sales

cleaned = sales_validation(sales)
print("Cleaned sales: ",cleaned)