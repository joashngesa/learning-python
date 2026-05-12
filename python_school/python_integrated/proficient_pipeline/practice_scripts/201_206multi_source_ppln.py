                            #MULTISOURCE ORDER INTAKE PIPELINE
#Pipeline task:
    #read file_a & file_b
    #convert both datasets
    #merge files
    #create is_valid check
    #extract invalid rows
    #extract cleaned rows
    #validate clean rows
        #calc revenue
        #group revenue
    #transform table
    #calc metrics
    #show output
    #write invalid and processed tables
    #create controller functions; multi_source_pipeline

            ##order_sys_a  delimiter is  ","
            ##order_sys_b delimiter is  "|"

import os
import csv
from tabulate import tabulate


def read_csv_files(file_path,delimiter):
    try:
        with open (file_path,"r",newline="") as file:
            reader = csv.DictReader (file,delimiter=delimiter)
            return list(reader)

    except FileNotFoundError:
        return None    
    
order_a_path = "C:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/source files/order_sys_a.csv"
order_b_path = "C:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/source files/order_sys_b.csv"
delimiter_a = ","
delimiter_b = "|"
                    #raw_order_a = read_csv_files(order_a_path,delimiter_a)
                    #raw_order_b = read_csv_files(order_b_path,delimiter_b)
                    #print(raw_order_a[:2])
                    #print(raw_order_b[:2])
                    #print(tabulate(raw_order_b, headers="keys",tablefmt="grid"))
#convert criteria
    #order_id → int
    #price → float
    #qty → int
    #invalid → None
def convert_raw_tbl(raw_order):
    converted = []
    for item in raw_order:
        new = item.copy()

        try:
            new["order_id"] = int(new["order_id"]) if new["order_id"] != "" else None
            new["price"] = float(new["price"]) if new["price"] != "" else None
            new["qty"] = int(new["qty"]) if new["qty"] != "" else None

        except ValueError:
            new["order_id"] = None
            new["price"] = None
            new["qty"] = None

        converted.append(new)   

    return converted    

                    #a_converted = convert_raw_tbl(raw_order_a)
                    #b_converted = convert_raw_tbl(raw_order_b)

                    #print(tabulate(a_converted, headers="keys",tablefmt="grid"))
                    #print(tabulate(b_converted, headers="keys",tablefmt="grid"))

def merge_tbls(a_converted,b_converted):
    merged_order_tbl = a_converted + b_converted
    return merged_order_tbl

                    #merged = merge_tbls(a_converted,b_converted)
                    #print(tabulate(merged, headers="keys",tablefmt="grid"))


#validation rules
    #all keys exist
    #price > 0
    #qty > 0
    #correct types
def is_valid_check(item):
    if not all (field in item for field in ["order_id","product","price","qty"]):
        return False
    
    order_id = item.get("order_id")
    price = item.get("price")
    qty = item.get("qty")

    if not isinstance (order_id,int):
        return False
    if not isinstance (price,(int,float)):
        return False
    if not isinstance (qty,int):
        return False
    if price <= 0 or qty <= 0:
        return False
    
    return True

def get_invalid_tbl(merged):
    return [item for item in merged if not is_valid_check(item)]

                    #invalids = get_invalid_tbl(merged)

def get_clean_tbl(merged):
    return [item for item in merged if is_valid_check(item)]

                    #cleaned = get_clean_tbl(merged)
                    #print(tabulate(invalids, headers="keys",tablefmt="grid"))
                    #print(tabulate(cleaned, headers="keys",tablefmt="grid"))

def get_validation(cleaned):
    for item in cleaned:
        if not is_valid_check(item):
            return False
        
    return True


def calc_revenue(item):
    return item.get("price") * item.get("qty")

#category rules
    #revenue > 1000 → "high"
    #revenue > 300 → "medium"
    #else → "low"

def group_revenue(item):
    revenue = calc_revenue(item)
    if revenue > 1000:
        return "high"
    if revenue > 300:
        return "medium"
    else:
        return "low"
    

#transformation
    #"order_id": ...,
    #"product": ...,
    #"revenue": price * qty,
    #"category"

def tbl_transformation(cleaned):
    return [
        {
            "order_id": item.get("order_id"),
            "product": item.get("product"),
            "revenue": calc_revenue(item),
            "category": group_revenue(item)
        }
        for item in cleaned
    ]

                    #transformed = tbl_transformation(cleaned)
                    #print(tabulate(transformed, headers="keys",tablefmt="grid"))
#metrics
    # "total_valid_orders": ...,
    #"total_revenue": ...,
    #"high_value_orders

def tot_valid_orders(transformed):
    return sum([1 for item in transformed])

                    #tvo = tot_valid_orders(transformed)
                    #print(tvo)

def high_value_orders(transformed):
    return [item for item in transformed if item.get("category") == "high"]
    
                    #highs = high_value_orders(transformed)
                    #print(tabulate(highs, headers="keys",tablefmt="grid"))

def tbl_metrics(transformed):
    tot_revenue = 0

    for item in transformed:
        tot_revenue += item.get("revenue")

    return [
        {
        "total_valid_orders": tot_valid_orders(transformed),#(i could do this or use len(cleaned), i was testing possibilities)
        "total_revenue": tot_revenue,
        "high_value_orders": high_value_orders(transformed)
        }
    ]

                    #metrics = tbl_metrics(transformed)
                    #print(tabulate(metrics, headers="keys",tablefmt="grid"))

def print_output(invalids,cleaned,transformed):
    print("\ninvalid table")
    print(tabulate(invalids, headers="keys",tablefmt="grid"))
    print("\ncleaned table")
    print(tabulate(cleaned, headers="keys",tablefmt="grid"))
    print("\ntransformed")
    print(tabulate(transformed, headers="keys",tablefmt="grid"))

                    #print_output(invalids,cleaned,transformed)

def write_csv_file(file_path,data,output_delimiter,column_names):
    with open (file_path,"w",newline="") as file:
        writer = csv.DictWriter (file,delimiter=output_delimiter,fieldnames=column_names)
        writer.writeheader()
        writer.writerows(data)
        print("write to: ",os.path.abspath(file_path))

invalid_tbl_columns = ["order_id","product","price","qty"]
transformed_tbl_columns = ["order_id","product","revenue","category"]

invalids_path = "C:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/order_sys_invalids.csv"
transformed_path = "C:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/order_sys_transformed.csv"
output_delimiter = "|"

def multi_source_pipeline(file_path_a,file_path_b,delimiter_a,delimiter_b):
    raw_order_a = read_csv_files(order_a_path,delimiter_a)
    raw_order_b = read_csv_files(order_b_path,delimiter_b)
    
    if raw_order_a is None:
        return {
            "status": "failed",
            "reason": "order_system_a file not found"
        }
    
    if raw_order_b is None:
        return {
            "status": "failed",
            "reason": "order_system_b file not found"
        }
    
    a_converted = convert_raw_tbl(raw_order_a)
    b_converted = convert_raw_tbl(raw_order_b)
    merged = merge_tbls(a_converted,b_converted)
    invalids = get_invalid_tbl(merged)
    cleaned = get_clean_tbl(merged)
    validation = get_validation(cleaned)

    if not validation:
        return {
            "status": "failed",
            "reason": "validation of cleaned data failed"
        }
    
    transformed = tbl_transformation(cleaned)
    metrics = tbl_metrics(transformed)
    print_output(invalids,cleaned,transformed)

    write_csv_file(invalids_path,invalids,output_delimiter,invalid_tbl_columns)
    write_csv_file(transformed_path,transformed,output_delimiter,transformed_tbl_columns)

    return {
        "status": "success",
        "metrics": metrics
    }

multi_source_pipeline(order_a_path,order_b_path,delimiter_a,delimiter_b)