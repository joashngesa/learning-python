#🎯 Case Scenario

#Raw sales order data from an operational system.

#The data is messy:

    #some rows are missing fields
    #some prices are invalid
    #some quantities are invalid

#pipeline goal:
        #get invalid rows
        #clean data
        #validate cleaned data
        #if validation fails, return a failure message
        #transform cleaned data
        #calculate metrics
        #return a structured result


#Upon successfull completion of the pipeline, print:(Final report)
    #"status": "success",
    #"invalid_count": ...,
    #"valid_count": ...,
    #"metrics": ...


orders = [
    {"id": 101, "product": "Laptop", "price": 1200, "qty": 1},
    {"id": 102, "product": "Mouse", "price": 25, "qty": 4},
    {"id": 103, "product": "Keyboard", "price": -80, "qty": 2},
    {"id": 104, "product": "Monitor", "qty": 2},
    {"id": 105, "product": "Dock", "price": 200, "qty": 0},
    {"id": 106, "product": "Headset", "price": 150, "qty": 3}
]

#🧱 BUSINESS RULES
#A record is valid only if:
    #it has "id"
    #it has "product"
    #it has "price"
    #it has "qty"
    #price > 0
    #qty > 0

#pipeline goal:
        #get invalid rows
        #clean data
        #validate cleaned data
        #if validation fails, return a failure message
        #transform cleaned data
        #calculate metrics
        #return a structured result
from tabulate import tabulate

def sales_pipeline(TITLE,table):

    def is_valid_tbl(item):
        if not all (key in item for key in ["id","product","price","qty"]):
            return False
        if not isinstance (item.get("id"),int):
            return False
        if not isinstance (item.get("price"),(int,float)):
            return False
        if not isinstance (item.get("qty"),int):
            return False
        if item.get("price") <= 0 or item.get("qty") <= 0:
            return False
        
        return True
        

    def invalid_tbl(table):
        return [item for item in table if not is_valid_tbl(item)]
    
    tbl_errors = invalid_tbl(table)
    
    def clean_data(table):
        return [item for item in table if is_valid_tbl(item)]
    
    cleaned = clean_data(table)
    if len(cleaned) == 0:
        output = {
            "status": "failed",
            "reason": "no valid records after cleaning"
        }
        print(output)
        return output

    def tbl_validation(cleaned):
        for item in cleaned:
            if not is_valid_tbl(item):
                return False
            
        return True
#Category rules
#revenue > 1000 → "high_value"
#revenue > 300 → "medium_value"
#else → "low_value"

    def calc_revenue(item):
        return item.get("price",0) * item.get("qty",0)
    
    def classify_revenue(item):
        revenue = calc_revenue(item)

        if revenue > 1000:
            return "high value"
        elif revenue > 300:
            return "medium value"
        else:
            return "low value"

    def transform_tbl(cleaned):
        return [
            {
                "id": item.get("id"),
                "product": item.get("product"),
                "price": item.get("price"),
                "quantity": item.get("qty"),
                "revenue": calc_revenue(item),
                "category": classify_revenue(item)
            }
            for item in cleaned
        ]
    transformed = transform_tbl(cleaned)

    #calculate total orders and total revenue

    def table_metrics(transformed):
        total_revenue = 0

        for item in transformed:
            total_revenue += item.get("revenue")

        return {
            "total orders": len(transformed),
            "total revenue": total_revenue
        }
    
    metrics = table_metrics(transformed)

    #print function should print:
    #status
    #invalid records
    #cleaned data
    #transformed data
    #metrics


    def print_tbl(TITLE,tbl_errors,cleaned,transformed):
        print(f"{TITLE}")
        print("\nInvalid records")
        print(tabulate(tbl_errors, headers = "keys", tablefmt = "grid"))
        print("\nCleaned table")
        print(tabulate(cleaned, headers = "keys", tablefmt = "grid"))
        print("\nTransformed table")
        print(tabulate(transformed, headers = "keys", tablefmt = "grid"))

       #invalid data:
    #"status": "failed",
    #"reason": "validation failed"

    validation = tbl_validation(cleaned)
    if not validation:
        output = {
            "status": "failed",
            "reason": "validation failed"
        }
        print (output)
        return output
    
    output = {
        "status": "success",
        "invalid records": tbl_errors,
        "invalid counts": len(tbl_errors),
        "valid records": cleaned,
        "valid counts": len(transformed),
        "transformed table": transformed,
        "table metrics": metrics
    }

    print("status: success.")
    print_tbl(TITLE,tbl_errors,cleaned,transformed)
    print("\nTable metrics: ",metrics)
    print("\nInvalid records count: ",len(tbl_errors))
    print("\nValid records count: ",len(transformed))

    return output

sales_pipeline("SALES PIPELINE",orders)


#Test examples
orders_empty = []

orders_all_bad = [
    {"id": 201, "product": "Laptop", "price": -100, "qty": 1},
    {"id": 202, "product": "Mouse", "qty": 2},
    {"id": 203, "price": 50, "qty": 2},
    {"product": "Dock", "price": 200, "qty": 0}
]

orders_one_good = [
    {"id": 301, "product": "Tablet", "price": 500, "qty": 2}
]

orders_zero_values = [
    {"id": 401, "product": "Laptop", "price": 0, "qty": 1},
    {"id": 402, "product": "Mouse", "price": 50, "qty": 0}
]

orders_boundaries = [
    {"id": 801, "product": "A", "price": 1000, "qty": 1},
    {"id": 802, "product": "B", "price": 150, "qty": 2},
    {"id": 803, "product": "C", "price": 301, "qty": 1}
]
sales_pipeline("empty",orders_empty)
sales_pipeline("bad orders",orders_all_bad)
sales_pipeline("zero values",orders_zero_values)
sales_pipeline("1_good",orders_one_good)
sales_pipeline("zero values",orders_all_bad)
sales_pipeline("order boundaries test",orders_boundaries)