                            #SCHEMA STANDARDIZITAION PIPILINE
#🗺️Function objective:
#1.read file x & y ▶️
#2.convert file x & y ▶️
#3.standardize file y to x standards ▶️
#4.merge files ▶️
#5.create is valid check ▶️
#6.get invalid tbl ▶️
#7.get valid tbl ▶️
#8.validate tbl ▶️
#9.calc revenue ▶️
#10.group revenue ▶️
    #create file source column ▶️
#11.get transformed tbl ▶️
#12.calc high value orders ▶️
#13.calc metrics ▶️
#14.create print output function ▶️
#15.write csv 
#16.exec_standardized_multi_source_file_ppln
#all functions with ▶️ have been tested

#🚩⚠️errors on the look out for;
    #missing files ❎
    #bad conversions ❎
    #empty datasets ❎
    #no valid records 🚩
    #wrong delimiter 🚩
    #path failures 🚩
#all errors❎ have been checked, all errors🚩 have not been addressed 

import os
import csv
from tabulate import tabulate

def read_csv_file(file_path,delimiter):
    try:
        with open (file_path,"r",newline="") as file:
            reader = csv.DictReader (file, delimiter=delimiter)
            return list (reader)
    
    except FileNotFoundError:
        return None
    
order_x_path = "C:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/source files/order_systems_x.csv"
order_y_path = "C:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/source files/order_systems_y.csv"
x_delimiter = ","
y_delimiter = ";"

                    #raw_orders_x = read_csv_file(order_x_path,x_delimiter)
                    #raw_orders_y = read_csv_file(order_y_path,y_delimiter)

                    #print(tabulate(raw_orders_x, headers="keys",tablefmt="grid"))
                    #print(tabulate(raw_orders_y, headers="keys",tablefmt="grid"))

def convert_x_orders(raw_orders_x):
    converted_x = []

    for unit in raw_orders_x:
        new = unit.copy()

        try:
            new["order_id"] = int(new["order_id"]) if new["order_id"] != "" else None
            new["price"] = int(new["price"]) if new["price"] != "" else None
            new["qty"] = int(new["qty"]) if new["qty"] != "" else None

        except ValueError:
            new["order_id"] = None
            new["price"] = None
            new["qty"] = None

        converted_x.append(new)

    return converted_x

                    #x_converted = convert_x_orders(raw_orders_x)
                    #print(tabulate(x_converted, headers="keys",tablefmt="grid"))

def convert_y_orders(raw_orders_y):
    converted_y = []

    for unit in raw_orders_y:
        new_y = unit.copy()

        try:
            new_y["id"] = int(new_y["id"]) if new_y["id"] != "" else None
            new_y["unit_price"] = int(new_y["unit_price"]) if new_y["unit_price"] != "" else None
            new_y["quantity"] = int(new_y["quantity"]) if new_y["quantity"] != "" else None

        except ValueError:
            new_y["id"] = None
            new_y["unit_price"] = None
            new_y["quantity"] = None

        converted_y.append(new_y)

    return converted_y

                    #y_converted = convert_y_orders(raw_orders_y)
                    #print(tabulate(y_converted, headers="keys",tablefmt="grid"))

def standardize_y(y_converted):
    y_standard = []
    for unit in y_converted:
        new_data = unit.copy()
        new_data ={
            "order_id": new_data.get("id"),
            "product": new_data.get("item_name"),
            "price": new_data.get("unit_price"),
            "qty": new_data.get("quantity"),
            "file_source": "file_y"
        }
        y_standard.append(new_data)

    return y_standard

                    #y_standard = standardize_y(y_converted)
                    #print(tabulate(y_standard, headers="keys",tablefmt="grid"))


def standardize_x(x_converted):
    x_standard = []
    for unit in x_converted:
        x_tbl = unit.copy()
        x_tbl = {
            "order_id": x_tbl.get("order_id"),
            "product": x_tbl.get("product"),
            "price": x_tbl.get("price"),
            "qty": x_tbl.get("qty"),
            "file_source": "file_x"
        }
        x_standard.append(x_tbl)

    return x_standard

                    #x_standard = standardize_x(x_converted)
                    #print(tabulate(x_standard, headers="keys",tablefmt="grid"))


def merge_orders(x_converted,y_standard):
    merged_tbls = x_converted + y_standard
    return merged_tbls                    

                    #merged = merge_orders(x_standard,y_standard)
                    #print(tabulate(merged, headers="keys",tablefmt="grid"))


#validation rules
    #order_id
    #product
    #price
    #qty
    #&
    #price > 0
    #qty > 0

def is_valid_check(unit):
    if not all (field in unit for field in ["order_id","product","price","qty","file_source"]):
        return False
    
    order_id = unit.get("order_id")
    price = unit.get("price")
    qty = unit.get("qty")

    if not isinstance (qty,int):
        return False
    if not isinstance (price,(float,int)):
        return False
    if not isinstance (order_id,int):
        return False
    if price <= 0 or qty <= 0:
        return False
    
    return True

def invalid_data(merged):
    return [unit for unit in merged if not is_valid_check(unit)]

                    #invalids = invalid_data(merged)
                    #print(tabulate(invalids, headers="keys",tablefmt="grid"))

def tbl_valids(merged):
    return [unit for unit in merged if is_valid_check(unit)]

                    #valids = tbl_valids(merged)
                    #print(tabulate(valids, headers="keys",tablefmt="grid"))

def validate_tbl(valids):
    for unit in valids:
        if not is_valid_check(unit):
            return False
        
    return True

                    #validate = validate_tbl(valids)
                    #print(validate)

def calc_revenue(unit):
    return unit.get("price") * unit.get("qty")

#category rules
    #revenue > 1000 → "high"
    #revenue > 300 → "medium"
    #else → "low"
def group_revenue(unit):
    revenue = calc_revenue(unit)
    if revenue > 1000:
        return "high"
    if revenue > 300:
        return "medium"
    else:
        return "low"
    


#transformation rules
    #"order_id": ...,
    #"product": ...,
    #"revenue": price * qty,
    #"category"    
def transform_tbl(valids):
    return [
        {
            "order_id": unit.get("order_id"),
            "product": unit.get("product"),
            "revenue": calc_revenue(unit),
            "category": group_revenue(unit)
        }
        for unit in valids
    ]

                    #transformed = transform_tbl(valids)
                    #print(tabulate(transformed, headers="keys",tablefmt="grid"))

def high_value_orders(transformed):
    return sum([1 for unit in transformed if unit.get("category") == "high"])

                    #highs = high_value_orders(transformed)
                    #print(highs)

#metrics
    #"total_valid_orders": ...,
    #"total_revenue": ...,
    #"high_value_orders
def calc_metrics(transformed):
    tot_revenue = 0

    for unit in transformed:
        tot_revenue += unit.get("revenue")

    return {
        "total valid orders": len(transformed),
        "total revenue": tot_revenue,
        "high value orders": high_value_orders(transformed)
    }

                    #metrics = calc_metrics(transformed)
                    #print(metrics)

def print_output(invalids,valids,transformed):
    print("\ninvalid data")
    print(tabulate(invalids, headers="keys",tablefmt="grid"))
    print("\nvalid data")
    print(tabulate(valids, headers="keys",tablefmt="grid"))
    print("\ntransformed")
    print(tabulate(transformed, headers="keys",tablefmt="grid"))

def write_csv_output(file_path,data,delimiter,column_names):
    with open (file_path, "w", newline="") as file:
        writer = csv.DictWriter (file,delimiter=delimiter,fieldnames=column_names)
        writer.writeheader()
        writer.writerows(data)
        print("write file to: ",os.path.abspath(file_path))

invalids_path = "C:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/pct105order_invalids.csv"
transformed_path = "C:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/pct105order_transformed.csv"
output_delimiter = ","
invalids_columns = ["order_id","product","price","qty","file_source"]
transformed_columns = ["order_id","product","revenue","category"]

def exec_standardized_multi_source_file_ppln(file_path1,file_path2,delimiter1,delimiter2):
    raw_orders_x = read_csv_file(file_path1,delimiter1)
    raw_orders_y = read_csv_file(file_path2,delimiter2)

    if raw_orders_x is None:
        return {
            "status": "failed",
            "reason": "order_x file not found"
        }
    if raw_orders_y is None:
        return{
             "status": "failed",
            "reason": "orders_y file not found"
        }
    
    x_converted = convert_x_orders(raw_orders_x)
    y_converted = convert_y_orders(raw_orders_y)

    if x_converted is None:
        return {
            "status": "failed",
            "reason": "conversion failed"
        }
    if y_converted is None:
        return {
            "status": "failed",
            "reason": "conversion failed"
        }
    y_standard = standardize_y(y_converted)
    x_standard = standardize_x(x_converted)
    merged = merge_orders(x_standard,y_standard)
    invalids = invalid_data(merged)
    valids = tbl_valids(merged)

    if len (valids) == 0:
        return {
            "status": "failed",
            "reason": "empty dataset"
        }

    validate = validate_tbl(valids)
    transformed = transform_tbl(valids)
    metrics = calc_metrics(transformed)
    print_output(invalids,valids,transformed)

    write_csv_output(invalids_path,invalids,output_delimiter,invalids_columns,)
    write_csv_output(transformed_path,transformed,output_delimiter,transformed_columns)

    return {
        "status": "success",
        "metrics": metrics
        }

exec_standardized_multi_source_file_ppln(order_x_path,order_y_path,x_delimiter,y_delimiter)
