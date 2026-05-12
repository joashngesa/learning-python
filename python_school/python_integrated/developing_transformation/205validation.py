
#def validate_cleaned_data(data):
#def calculate_metrics(data):
#get_invalid_records(data) returns all bad rows
#bad row means:
#missing "id" OR
#missing "price" OR
#price <= 0
#clean_data(data) returns only valid rows
#validate_cleaned_data(data) returns True/False
#calculate_metrics(data) returns:
#total_revenue
#valid_items

#Then run a pipeline that prints:

#invalid records
#cleaned records
#metrics if cleaned data is valid
sales = [
    {"id": 1, "price": 500},
    {"id": 2, "price": -100},
    {"price": 300},
    {"id": 4, "price": 200}
]
def get_invalid_records(sales):
    return [pdct for pdct in sales if "price" not in pdct or "id" not in pdct or pdct.get("price",0) <= 0]

def clean_data(sales):
    return [pdct for pdct in sales if "price" in pdct and "id" in pdct and  pdct.get("price",0) > 0]

def validate_cleaned_data(cleaned):
    for pdct in cleaned:
        if "price" not in pdct or "id" not in pdct or pdct.get("price",0) <= 0:
            return False
    
    return True

def calc_revenue(cleaned):
    revenue = 0
    for pdct in cleaned:
        revenue += pdct.get("price",0)
    return {
        "Revenue": revenue,
        "Valid items": len(cleaned)
    }
        
cleaned = clean_data(sales)
invalid_tbl = get_invalid_records(sales)
validation = validate_cleaned_data(cleaned)

if validation:
    tot_sales = calc_revenue(cleaned)
    print("Pipeline executed!")
    print("Invalid records: ",invalid_tbl)
    print("Processed records: ",cleaned)
    print(tot_sales)
else:
    print("The pipeline did not execute.")


