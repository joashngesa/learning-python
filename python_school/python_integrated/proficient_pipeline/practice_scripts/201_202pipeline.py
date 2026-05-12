            #INVENTORY REPLENISHMENT READINESS
#Create one pipeline that:
    #detects invalid rows
    #cleans valid rows
    #validates cleaned rows
    #transforms valid rows into business-ready replenishment output
    #calculates summary metrics
    #returns a structured result
from tabulate import tabulate

inventory = [
    {"sku": "A100", "product": "Laptop Stand", "units_in_stock": 8, "reorder_point": 10, "unit_cost": 25},
    {"sku": "B200", "product": "Wireless Mouse", "units_in_stock": 40, "reorder_point": 15, "unit_cost": 18},
    {"sku": "C300", "product": "Keyboard", "units_in_stock": 0, "reorder_point": 12, "unit_cost": 30},
    {"sku": "D400", "product": "Monitor", "reorder_point": 5, "unit_cost": 120},
    {"sku": "E500", "product": "USB Dock", "units_in_stock": 12, "reorder_point": 12, "unit_cost": 60},
    {"sku": "F600", "product": "Headset", "units_in_stock": 3, "reorder_point": 8, "unit_cost": -15},
    {"sku": "G700", "product": "Webcam", "units_in_stock": 25, "reorder_point": 10, "unit_cost": 45}
]
#print(tabulate(inventory, headers = "keys", tablefmt = "grid"))

#Pipeline should:
    #get invalid records
    #clean data
    #validate cleaned data
    #fail early if validation fails
    #transform valid rows
    #calculate metrics
    #return structured output

#Failure outcome shape   
    #"status": "failed",
    #"reason": "validation failed"

#🧱 Business rules
    #"sku"
    #"product"
    #"units_in_stock"
    #"reorder_point"
    #"unit_cost"
        #units_in_stock >= 0
        #reorder_point > 0
        #unit_cost > 0

def inventory_pipeline(TITLE,table):

    def is_valid_tbl(stock):
        if not all (key in stock for key in ["sku","product","units_in_stock","reorder_point","unit_cost"]):
            return False
        
        stk_units = stock.get("units_in_stock")
        stk_reorder = stock.get("reorder_point")
        stk_cost = stock.get("unit_cost")
        
        if not isinstance (stk_units,int):
            return False
        if not isinstance (stk_reorder,int):
            return False
        if not isinstance (stk_cost,(int,float)):
            return False
        if stk_units < 0 or stk_reorder <= 0 or stk_cost <= 0:
            return False
        
        return True
            
    def invalid_data(table):
        return [stock for stock in table if not is_valid_tbl(stock)]
    
    invalids = invalid_data(table)

    def cleaning_tbl(table):
        return [stock for stock in table if is_valid_tbl(stock)]
    
    cleaned = cleaning_tbl(table)
    
    if len(cleaned) == 0:
        output = {
            "status": "pipelined failed",
            "reason": "no or invalid data to clean"
        }
        print(output)
        return output
    
    def tbl_validation(cleaned):
        for stock in cleaned:
            if not is_valid_tbl(stock):
                return False
        return True
    
    validation = tbl_validation(cleaned)

    #Valid transformed rows should contain
        #sku
        #product
        #inventory_value = units_in_stock * unit_cost
        #reorder_needed
        #stock_status

    def inventory_value(stock):
        return stock.get("units_in_stock") * stock.get("unit_cost")
    
    #Logic for transformation
    #reorder_needed
    #True if units_in_stock < reorder_point
    #False otherwise

    def calc_reorder_needed(stock):
        if stock.get("units_in_stock") < stock.get("reorder_point"):
            return True
        
        return False

    #stock_status
    #"critical" if units_in_stock == 0
    #"low" if units_in_stock < reorder_point
    #"healthy" otherwise

    def stock_status_categories(stock):
        if stock.get("units_in_stock") == 0:
            return "critical"
        if stock.get("units_in_stock") < stock.get("reorder_point"):
            return "low"
        else:
            return "healthy"
        
    #Intended transformed output table:
    #"sku": "A100",
    #"product": "Laptop Stand",
    #"inventory_value": 200,
    #"reorder_needed": True,
    #"stock_status": "low"

    def transform_tbl(cleaned):
        return [
            {
                "sku": stock.get("sku"),
                "product": stock.get("product"),
                "inventory_value": inventory_value(stock),
                "reorder_needed": calc_reorder_needed(stock),
                "stock_status": stock_status_categories(stock)
            }
            for stock in cleaned
        ]
    
    transformed = transform_tbl(cleaned)

    def calc_reorder_count(transformed):
        reorder_count = 0
        for stock in transformed:
            if stock.get("reorder_needed") == True:
                reorder_count += 1

        return reorder_count

    #Intended metrics return
    #"total_valid_items": ...,(number of transformed rows)
    #"total_inventory_value"(sum of inventory value)
    #"reorder_count"(how many rows have reorder needed == true)

    def tbl_metrics(transformed):
        inventory_value_sum = 0
        for stock in transformed:
            inventory_value_sum += stock.get("inventory_value")

        return {
            "total_valid_items": len(transformed),
            "total_inventory_value": inventory_value_sum,
            "reorder_count": calc_reorder_count(transformed)
        }
    
    metrics = tbl_metrics(transformed)

    #Success outcome shape
    #"status": "success",
    #"invalid_records": ...,
    #"cleaned_data": ...,
    #"transformed_data": ...,
    #"metrics": ...

    def show_output(TITLE,invalids,cleaned,transformed,metrics):
        print(f"{TITLE}")
        print("\nInvalid data table")
        print(tabulate(invalids, headers = "keys", tablefmt = "grid"))
        print("\nCleaned table")
        print(tabulate(cleaned, headers = "keys", tablefmt = "grid"))
        print("\nTransformed table")
        print(tabulate(transformed, headers = "keys", tablefmt = "grid"))
        print("Inventory metrics",metrics)

    if not validation:
        output = {
            "status": "pipeline execution failed",
            "reason": "data validation failed"
        }
        print(output)
        return output
    
    output = {
        "status": "success",
        "invalid records": invalids,
        "cleaned data": cleaned,
        "transformed data": transformed,
        "inventory data metrics": metrics
    }

    print("status: success")
    show_output("Inventory Pipeline",invalids,cleaned,transformed,metrics)

    return output

inventory_pipeline("INVENTORY REPLENISHMENT DATA",inventory)