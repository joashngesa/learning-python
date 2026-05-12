#SUPPLIER INVENTORY FEED PIPELINE

import csv
import os
from tabulate import tabulate

def read_csv_file(input_path,delimiter):
    try:
        with open (input_path,"r",newline="")as file:
            reader = csv.DictReader (file,delimiter=delimiter)
            return list(reader)

    except FileNotFoundError:
        return None
input_path = "C:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/source files/pct102_supplier_inventory_feed.csv"

                    #raw_supplier_inv = read_csv_file(input_path,"|")
                    #print(raw_supplier_inv[:2])

    
#Convert rules:
#units_in_stock → int
#reorder_point → int
#unit_cost → float
#Rules:
#blank string → None
#invalid conversion (like "abc") → None
def convert_data(raw_supplier_inv):
    converted_data = []

    for stock in raw_supplier_inv:
        new_data = stock.copy()
      
        try:
            new_data["units_in_stock"] = int(new_data.get("units_in_stock")) if new_data.get("units_in_stock") != "" else None
            new_data["reorder_point"] = int(new_data.get("reorder_point")) if new_data.get("reorder_point") != "" else None
            new_data["unit_cost"] = float(new_data.get("unit_cost")) if new_data.get("unit_cost") != "" else None
        except ValueError:
            new_data["units_in_stock"] = None
            new_data["reorder_point"] = None
            new_data["unit_cost"] = None

        converted_data.append(new_data)
    return converted_data

                    #converted = convert_data(raw_supplier_inv)    
                    #print(tabulate(converted, headers="keys",tablefmt="grid"))
#Validation rules:
#table must have: sku,product,units_in_stock,reorder_point,unit_cost and:
#units_in_stock >= 0, reorder_point > 0, unit_cost > 0
def is_valid_tbl(stock):
    if not all (keys in stock for keys in ["sku","product","units_in_stock","reorder_point","unit_cost"]):
        return False
    units_in_stock = stock.get("units_in_stock")
    reorder_point = stock.get("reorder_point")
    unit_cost = stock.get("unit_cost")

    if not isinstance (units_in_stock,int):
        return False
    if not isinstance (reorder_point,int):
        return False
    if not isinstance (unit_cost,(int,float)):
        return False
    if units_in_stock < 0 or reorder_point <= 0 or unit_cost <= 0:
        return False
    
    return True

def invalid_tbl(converted):
    return [stock for stock in converted if not is_valid_tbl(stock)]
                    #invalids = invalid_tbl(converted)
                    #print(tabulate(invalids, headers="keys",tablefmt="grid"))

def valid_tbl(converted):
    return  [stock for stock in converted if is_valid_tbl(stock)]
                    #cleaned = valid_tbl(converted)
                    #print(tabulate(cleaned, headers="keys",tablefmt="grid"))

def tbl_validation(cleaned):
    for stock in cleaned:
        if not is_valid_tbl(stock):
            return False
        
    return True
                    #validation = tbl_validation(cleaned)

def calc_inventory_value(stock):
    return stock.get("units_in_stock") * stock.get("unit_cost")

def get_reorder_needed(stock):
    if stock.get("units_in_stock") < stock.get("reorder_point"):
        return True
    else:
        return False

#stock_status: "critical" if units_in_stock == 0,"low" if units_in_stock < reorder_point,"healthy" otherwise
def get_stock_status(stock):
    if stock.get("units_in_stock") == 0:
        return "critical"
    if stock.get("units_in_stock") < stock.get("reorder_point"):
        return "low"
    else:
        return "healthy"

#transformed columns;"sku","product","inventory_value","reorder_needed","stock_status"
def transform_tbl(cleaned):
    return  [
        {
            "sku": stock.get("sku"),
            "product": stock.get("product"),
            "inventory_value": calc_inventory_value(stock),
            "reorder_needed": get_reorder_needed(stock),
            "stock_status": get_stock_status(stock)
        }
        for stock in cleaned
    ]
                    #transformed = transform_tbl(cleaned)
                    #print(tabulate(transformed, headers="keys",tablefmt="grid"))

def reorder_count(transformed):
    return sum([1 for stock in transformed if stock.get("reorder_needed") is True])
                    #reorder_check = reorder_count(transformed)
                    #print(reorder_check)    

#metrics to return = {"total_valid_items":"total_inventory_value":"reorder_count"
def tbl_metrics(transformed):
    tot_inventory = 0

    for stock in transformed:
        tot_inventory += stock.get("inventory_value")

    return {
        "total valid items": len(transformed),
        "total_inventory_value": tot_inventory,
        "reorder_count": reorder_count(transformed)
    }
                    #metrics = tbl_metrics(transformed)
                    #print(metrics)

def print_tbl(invalids,transformed):
    print("invalid table\n")
    print(tabulate(invalids, headers="keys", tablefmt="grid"))
    print("\nTransformed table")
    print(tabulate(transformed, headers="keys", tablefmt="grid"))

                    #show_output = print_tbl(invalids,cleaned)
                    #print(show_output)

invalid_file_path = "C:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/pct102invalids_supplier_inventory.csv"
transformed_file_path = "C:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/pct102_transformed_supplier_inventory.csv"

def write_csv(filepath,data,column_names,delimiter="|"):
    with open (filepath,"w",newline="")as file:
        writer = csv.DictWriter(file,fieldnames=column_names,delimiter=delimiter)
        writer.writeheader()
        writer.writerows(data)
    print("writing file to:",os.path.abspath(filepath))
invalids_columns = ["sku","product","units_in_stock","reorder_point","unit_cost"]
transformed_columns = ["sku","product","inventory_value","reorder_needed","stock_status"]

def file_inventory_pipeline(input_path,delimiter="|"):
    raw_supplier_inv = read_csv_file(input_path,delimiter)

    if raw_supplier_inv is None:
        return {
            "status": "failed",
            "reason": "could  not find source file"
        }
    converted = convert_data(raw_supplier_inv)
    invalids = invalid_tbl(converted)
    cleaned = valid_tbl(converted)

    if len(cleaned) == 0:
        return {
            "status": "failed",
            "reason": "no valid data"
        }
    
    validation = tbl_validation(cleaned)
    if not validation:
        return {
            "status": "failed",
            "reason": "validation failed"
        }
    
    transformed = transform_tbl(cleaned)
    metrics = tbl_metrics(transformed)
    print_tbl(invalids,transformed)
   
   
    write_csv(invalid_file_path,invalids,invalids_columns,delimiter)
    write_csv(transformed_file_path,transformed,transformed_columns,delimiter)

    return {
        "status": "success",
        "metrics": metrics
    }


file_inventory_pipeline(input_path,"|")
    



