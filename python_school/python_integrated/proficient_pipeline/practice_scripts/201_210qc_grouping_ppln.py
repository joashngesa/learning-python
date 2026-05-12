                            #PRODUCT INVENTORY QUALITY PIPELINE
#pipeline plan:
    #convert raw ▶️
    #validate converted
        #create validation function ▶️
        #get valids and invalids ▶️
    #transform data ▶️
        #create stock level column ▶️
        #create inventory value ▶️
    #get metrics ▶️
        #high_stock_count ▶️
        #medium_stock_count ▶️
        #low_stock_count ▶️
    #create error summary ▶️
    #create error summary by warehouse ▶️
#create show output function ▶️
    #write csv files ▶️

import os
import csv
from tabulate import tabulate

raw_inventory = [
    {"item_id": "I001", "warehouse": "W1", "category": "electronics", "quantity": "50", "unit_cost": "300", "supplier": "S1"},
    {"item_id": "I002", "warehouse": "W1", "category": "furniture", "quantity": "-5", "unit_cost": "120", "supplier": "S2"},
    {"item_id": "I003", "warehouse": "W2", "category": "", "quantity": "20", "unit_cost": "80", "supplier": "S1"},
    {"item_id": "I004", "warehouse": "W2", "category": "electronics", "quantity": "abc", "unit_cost": "200", "supplier": "S3"},
    {"item_id": "I005", "warehouse": "W3", "category": "clothing", "quantity": "100", "unit_cost": "25", "supplier": "S2"},
    {"item_id": "I006", "warehouse": "W3", "category": "toys", "quantity": "40", "unit_cost": "15", "supplier": "S4"},
    {"item_id": "I001", "warehouse": "W1", "category": "electronics", "quantity": "70", "unit_cost": "300", "supplier": "S1"},
    {"item_id": "I008", "warehouse": "W2", "category": "furniture", "quantity": "10", "unit_cost": "xyz", "supplier": "S2"},
]
                    #print(tabulate(raw_inventory, headers="keys", tablefmt="grid"))


def convert_raw_data(raw_file):
    converted_data = []
    for stock in raw_file:
        new = stock.copy()
        try:
            new["quantity"] = int(new["quantity"]) if new["quantity"] != "" else None      

        except ValueError:
             new["quantity"] = None

        try:
            new["unit_cost"] = int(new["unit_cost"]) if new["unit_cost"] != "" else None

        except ValueError:
            new["unit_cost"] = None
        
        converted_data.append(new)
    return converted_data

                    #converted = convert_raw_data(raw_inventory)
                    #print(tabulate(converted, headers="keys", tablefmt="grid"))


#validation rules
    #item_id: non-empty string
    #warehouse: one of W1, W2, W3
    #category: non-empty string and one of electronics, furniture, clothing
    #quantity: integer greater than 0
    #unit_cost: integer greater than 0
    #supplier: non-empty string
    #item_id must not be duplicated

raw_columns = ["item_id","warehouse","category","quantity","unit_cost","supplier"]
def validate_data(stock):
    for column in raw_columns:
        if column not in stock:
            return False, f"the column {column} is not found"
    
    item_id = stock.get("item_id")
    warehouse = stock.get("warehouse")
    category = stock.get("category")
    quantity = stock.get("quantity")
    unit_cost = stock.get("unit_cost")
    supplier = stock.get("supplier")

    categories_allowed = ["electronics","furniture","clothing"]
    warehouses_allowed = ["W1","W2","W3"]

    if not isinstance (item_id,str) or item_id == "":
        return False, "the item_id needs to be a non_empty string"
    if warehouse not in warehouses_allowed:
        return False, "warehouse accepted are only W1,W2,W3"
    if not isinstance (warehouse,str) or warehouse == "":
        return False, "warehouse needs to be a non_empty string"
    if category not in categories_allowed:
        return False, "categories only allowed records are electronics,furniture,clothing"
    if not isinstance (quantity,int):
        return False, "quantity should be integer"
    if quantity <= 0:
        return False, "quantity should be greater than zero"
    if not isinstance (unit_cost,int):
        return False, "unit_cost should be integer"
    if unit_cost <= 0:
        return False, "unit_cost should be greater than zero"
    if not isinstance (supplier,str) or supplier == "":
        return False, "supplier needs to be a non_empty string"
    
    return True,None

def split_invalids_valids(converted):
    invalids = []
    valids = []
    seen_ids = set()

    for stock in converted:
        is_valid, reason = validate_data(stock)

        if not is_valid:
            invalid_data = stock.copy()
            invalid_data["error_reason"] = reason
            invalids.append(invalid_data)
            continue
        item_id = stock.get("item_id")

        if item_id in seen_ids:
            invalid_data = stock.copy()
            invalid_data["error_reason"] = "duplicate stock"
            invalids.append(invalid_data)
            continue

        seen_ids.add(item_id)
        valids.append(stock)

    return invalids,valids

                    #invalids,valids = split_invalids_valids(converted)
                    #print(tabulate(valids, headers="keys", tablefmt="grid"))
                    #print(tabulate(invalids, headers="keys", tablefmt="grid"))     

def inventory_value(stock):
    return stock.get("quantity") * stock.get("unit_cost")


#stock level
    #quantity >= 80 → high_stock
    #quantity >= 30 → medium_stock
    #else → low_stock
def group_stock_level(stock):
    if stock.get("quantity") >= 80:
        return "high_stock"
    if stock.get("quantity") >= 30:
        return "medium_stock"
    else:
        return "low_stock"

#transformation rules...inventory_value = quantity * unit_cost
    #item_id
    #warehouse
    #category
    #quantity
    #unit_cost
    #inventory_value
    #stock_level
def transform_data(valids):
    return [
        {
            "item_id": stock.get("item_id"),
            "warehouse": stock.get("warehouse"),
            "category": stock.get("category"),
            "quantity": stock.get("quantity"),
            "unit_cost": stock.get("unit_cost"),
            "inventory_value": inventory_value(stock),
            "stock_level": group_stock_level(stock)
        }
        for stock in valids
    ]

                    #transformed = transform_data(valids)
                    #print(tabulate(transformed, headers="keys", tablefmt="grid"))    

#metrics output
    #"total_valid_items": ...,
    #"total_inventory_value": ...,
    #"high_stock_count": ...,
    #"medium_stock_count": ...,
    #"low_stock_count": ...

def high_stock_count(transformed):
    return sum([1 for stock in transformed if stock.get("stock_level") == "high_stock"])

                    #hsc = high_stock_count(transformed)
                    #print(hsc)

def medium_stock_count(transformed):
    return sum([1 for stock in transformed if stock.get("stock_level") == "medium_stock"])
    
                    #msc = medium_stock_count(transformed)
                    #print(msc)

def low_stock_count(transformed):
    return sum([1 for stock in transformed if stock.get("stock_level") == "low_stock"])

                    #lsc = low_stock_count(transformed)
                    #print(lsc) 

def metrics_data(transformed):
    tot_inventory_value = 0

    for stock in transformed:
        tot_inventory_value += stock.get("inventory_value")

    return [
    {
        "total_valid_items": len(transformed),
        "total_inventory_values": tot_inventory_value,
        "high_stock_count": high_stock_count(transformed),
        "medium_stock_count": medium_stock_count(transformed),
        "low_stock_count": low_stock_count(transformed)
    }
    ]
                    #metrics = metrics_data(transformed)
                    #print(tabulate(metrics, headers="keys", tablefmt="grid"))

#error_summary output
def error_summary(invalids):
    error_sum = {}
    for stock in invalids:
        reason = stock.get("error_reason")

        if reason not in error_sum:
            error_sum[reason] = 1
        else:
            error_sum[reason] += 1
        
    summary_tbl = [{"error_reason": reason , "count": count}
                   for reason, count in error_sum.items()]
    
    return summary_tbl
    
                    #error_notes = error_summary(invalids)
                    #print(tabulate(error_notes, headers="keys", tablefmt="grid"))

#error summary by warehouse output
def errors_by_warehouse(invalids):
    errors_warehouse_list = {}
    for stock in invalids:
        warehouse = stock.get("warehouse")
        reason = stock.get("error_reason")
        keys = (warehouse,reason)

        if keys not in errors_warehouse_list:
            errors_warehouse_list[keys] = 1
        else:
            errors_warehouse_list[keys] += 1
        
    error_wh = []

    for keys, count in errors_warehouse_list.items():
        warehouse, reason = keys
        error_wh.append({
                "warehouse": warehouse,
                "error_reason": reason,
                "count": count
            })

    return error_wh

                    #warehouse_errors = errors_by_warehouse(invalids)
                    #print(tabulate(warehouse_errors, headers="keys", tablefmt="grid"))

def show_output(invalids,valids,transformed,metrics,error_notes,warehouse_errors):
    print("\ninvalid_table")
    print(tabulate(invalids, headers="keys", tablefmt="grid"))
    print("\nvalid_table")
    print(tabulate(valids, headers="keys", tablefmt="grid"))
    print("\ntransformed_table")
    print(tabulate(transformed, headers="keys", tablefmt="grid"))
    print("\nmetrics")
    print(tabulate(metrics, headers="keys", tablefmt="grid"))
    print("\nerror_summary")
    print(tabulate(error_notes, headers="keys", tablefmt="grid"))
    print("\nerror summary by warehouse")
    print(tabulate(warehouse_errors, headers="keys", tablefmt="grid"))


def write_csv_file(file_path,data,output_delimiter,output_columns):
    folder_path = os.path.dirname (file_path)

    if folder_path:
            os.makedirs(folder_path,exist_ok=True)

    with open (file_path, "w", newline="") as file:
        writer = csv.DictWriter (file,delimiter=output_delimiter,fieldnames=output_columns,extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)
        print("write to: ",os.path.abspath(file_path))

#csv files to write
    #inventory_invalids.csv
    #inventory_valids.csv
    #inventory_processed.csv
    #inventory_metrics.csv
    #inventory_quality_report.csv
    #inventory_error_summary.csv
    #inventory_error_by_warehouse.csv

invalids_path = "c:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/pdct_inventory_qc/invalids.csv"
valids_path = "c:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/pdct_inventory_qc/valids.csv"
processed_path = "c:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/pdct_inventory_qc/processed.csv"
metrics_path = "c:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/pdct_inventory_qc/output_metrics.csv"
errors_path = "c:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/pdct_inventory_qc/output_errors.csv"
wh_error_path = "c:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/pdct_inventory_qc/wh_error.csv"

invalid_column = ["item_id","warehouse","category","quantity","unit_cost","supplier","error_reason"]
valid_columns = ["item_id","warehouse","category","quantity","unit_cost","supplier"]
processed_columns = ["item_id","warehouse","category","quantity","unit_cost","inventory_value","stock_level"]
metrics_columns = ["total_valid_items","total_inventory_values","high_stock_count","medium_stock_count","low_stock_count"]
errors_column = ["error_reason","count"]
wh_error_column = ["warehouse","error_reason","count"]


def exec_write_csv_inventory_qc_pipeline(raw_file,output_delimiter):
    converted = convert_raw_data(raw_file)
    if converted is None:
        return {
            "status": "failed",
            "reason": "conversion failed"
        }
    
    invalids,valids = split_invalids_valids(converted)
    transformed = transform_data(valids)
    metrics = metrics_data(transformed)
    error_notes = error_summary(invalids)
    warehouse_errors = errors_by_warehouse(invalids)
    show_output(invalids,valids,transformed,metrics,error_notes,warehouse_errors)
    write_csv_file(invalids_path,invalids,output_delimiter,invalid_column)
    write_csv_file(valids_path,valids,output_delimiter,valid_columns)
    write_csv_file(processed_path,transformed,output_delimiter,processed_columns)
    write_csv_file(metrics_path,metrics,output_delimiter,metrics_columns)
    write_csv_file(errors_path,error_notes,output_delimiter,errors_column)
    write_csv_file(wh_error_path,warehouse_errors,output_delimiter,wh_error_column)

    return {
        "status": "success",
        "metrics": metrics
    }


exec_write_csv_inventory_qc_pipeline(raw_inventory,"|")