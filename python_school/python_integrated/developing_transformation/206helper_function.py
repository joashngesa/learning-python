from tabulate import tabulate

sales = [
    {"id": 1, "price": 500},
    {"id": 2, "price": -100},
    {"price": 300},
    {"id": 4, "price": 200}
]
def is_valid_records(product):
    return "id" in product and "price" in product and product.get("price",0) > 0

def get_invalid_records(sales):
    return [product for product in sales if not is_valid_records(product)]

def clean_data(sales):
    return [product for product in sales if is_valid_records(product)]

def validate_cleaned_data(cleaned):
    for product in cleaned:
        if not is_valid_records(product):
            return False
        
    return True


def calc_revenue(cleaned):
    revenue = 0
    for product in cleaned:
        revenue += product.get("price",0)
    return {
        "Revenue": revenue,
        "Valid items": len(cleaned)
    }
        
cleaned = clean_data(sales)
invalid_tbl = get_invalid_records(sales)
validation = validate_cleaned_data(cleaned)

if not validation:
     print("The pipeline did not execute.")
else:
    tbl_metrics = calc_revenue(cleaned)
    print("Pipeline executed!")
    print("Invalid Table")
    print(tabulate(invalid_tbl, headers = "keys", tablefmt = "grid"))
    print("Cleaned Table")
    print(tabulate(cleaned, headers = "keys", tablefmt = 'grid'))
    print(tbl_metrics)
   

    