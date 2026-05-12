                            #SHIPMENT DELIVERY PERFORMANCE PIPELINE
#pipeline task;
#reads the shipment file 
#converts data types
#detect invalid rows
#keeps valid rows
#validates cleaned rows
#transforms valid rows into business-ready output
#calculates shipment metrics
#writes invalid and processed files

import os
import csv
from tabulate import tabulate

def read_csv_file(filepath,delimiter):
    try:
        with open (filepath, "r", newline="")as file:
            reader = csv.DictReader (file,delimiter=delimiter)
            return list(reader)
    except FileNotFoundError:
        return None
    
input_path = "C:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/source files/pct103_shipment_delivery_feed.csv"    
                    #raw_shipment_delivery = read_csv_file(input_path,",")
                    #print(tabulate(raw_shipment_delivery, headers="keys", tablefmt="grid"))
#conversion rules:
    #shipment_id → int
    #planned_days → int
    #actual_days → int
    #shipping_cost → float
    # Rules:
    #blank string → None
    #invalid conversion like "abc" → None
def convert_raw_tbl(raw_shipment_delivery):
    converted_tbl = []
    for shpt in raw_shipment_delivery:
        new = shpt.copy()
        try:
            new["shipment_id"] = int( new["shipment_id"]) if  new["shipment_id"] != "" else None
            new["planned_days"] = int(new["planned_days"]) if new["planned_days"] != "" else None
            new["actual_days"] = int(new["actual_days"]) if new["actual_days"] != "" else None
            new["shipping_cost"] = float(new["shipping_cost"]) if new["shipping_cost"] != "" else None 

        except ValueError:
            new["shipment_id"] = None
            new["planned_days"] = None
            new["actual_days"] = None
            new["shipping_cost"] = None 

        converted_tbl.append(new) 

    return converted_tbl

                    #converted = convert_raw_tbl(raw_shipment_delivery)
                    #print(tabulate(converted, headers="keys", tablefmt="grid"))

    #A row is valid only if it has:
    #shipment_id
    #route
    #planned_days
    #actual_days
    #shipping_cost
    #&:
    #planned_days > 0
    #actual_days > 0
    #shipping_cost > 0
def is_valid_check(shpt):
    if not all (keys in shpt for keys in ["shipment_id","route","planned_days","actual_days","shipping_cost"]):
        return False
    shpt_id = shpt.get("shipment_id") 
    planned_days = shpt.get("planned_days")
    actual_days = shpt.get("actual_days")
    shpn_cost = shpt.get("shipping_cost")

    if not isinstance (shpt_id,int):
        return False
    if not isinstance (planned_days,int):
        return False
    if not isinstance (actual_days,int):
        return False
    if not isinstance (shpn_cost,(int,float)):
        return False
    if planned_days <= 0 or actual_days <= 0 or shpn_cost <= 0:
        return False
    
    return True

def get_invalid_tbl(converted):
    return [shpt for shpt in converted if not is_valid_check(shpt)]

                    #invalids = get_invalid_tbl(converted)
                    #print(tabulate(invalids, headers="keys", tablefmt="grid"))


def get_valid_tbl(converted):
    return [shpt for shpt in converted if is_valid_check(shpt)]

                    #cleaned = get_valid_tbl(converted)
                    #print(tabulate(cleaned, headers="keys", tablefmt="grid"))

def tbl_validation(cleaned):
    for shpt in cleaned:
        if not is_valid_check(shpt):
            return False
        
    return True

#Delivery business logic
    #delay_days = actual_days - planned_days
def calc_delay_days(shpt):
    return shpt.get("actual_days") - shpt.get("planned_days")

#delivery_status
    #Rules:
    #"early" if actual_days < planned_days
    #"on_time" if actual_days == planned_days
    #"late" if actual_days > planned_days
def calc_delivery_status(shpt):
    if shpt.get("actual_days") < shpt.get("planned_days"):
        return "early"
    if shpt.get("actual_days") == shpt.get("planned_days"):
        return "on_time"
    if shpt.get("actual_days") > shpt.get("planned_days"):
        return "late"
    
#Transformation logic
    #"shipment_id": ...,
    #"route": ...,
    #"delay_days": ...,
    #"delivery_status": ...,
    #"shipping_cost": ...
def transform_tbl(cleaned):
    return [
        {
            "shipment_id": shpt.get("shipment_id"),
            "route": shpt.get("route"),
            "delay_days": calc_delay_days(shpt),
            "delivery_status": calc_delivery_status(shpt),
            "shipping_cost": shpt.get("shipping_cost")
        }
        for shpt in cleaned
    ]

                    #transformed = transform_tbl(cleaned)
                    #print(tabulate(transformed, headers="keys", tablefmt="grid"))

def calc_late_deliveries(transformed):
    return sum([1 for shpt in transformed if str(shpt.get("delivery_status")).lower() == "late"])

#metrics to calculate:
    #total_valid_shipments = number of transformed rows
    #late_shipments = count where delivery_status == "late"
    #total_shipping_cost = sum of shipping_cost
def tbl_metrics(transformed):
    tot_shipping_cost = 0

    for shpt in transformed:
        tot_shipping_cost += shpt.get("shipping_cost")

    return {
        "Total valid shipments": len(transformed),
        "Total number of late shipments": calc_late_deliveries(transformed),
        "Total shipping cost": tot_shipping_cost
    }

def tree_output(invalids,cleaned,transformed):
    print("\nInvalid table")
    print(tabulate(invalids, headers="keys", tablefmt="grid"))
    print("\ncleaned table")
    print(tabulate(cleaned, headers="keys", tablefmt="grid"))
    print("\ntransformed table")
    print(tabulate(transformed, headers="keys", tablefmt="grid"))
   

def write_csv_file(filepath,data,column_names,delimiter):
    with open (filepath, "w", newline="") as file:
        writer = csv.DictWriter (file,fieldnames=column_names,delimiter=delimiter)
        writer.writeheader()
        writer.writerows(data)
        print("writing file to: ",os.path.abspath(filepath))

output_invalids_path = "C:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/pct103invalids_delivery.csv"
output_transformed_path = "C:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/pct103transformed_delivery.csv"

invalid_columns = ["shipment_id","route","planned_days","actual_days","shipping_cost"]
transformed_columns = ["shipment_id","route","delay_days","delivery_status","shipping_cost"]

def delivery_file_pipeline(filepath,delimiter=","):
    raw_shipment_delivery = read_csv_file(filepath,",")

    if raw_shipment_delivery is None:
        return {
            "status": "failed",
            "reason": "file could not be found from source"
        }

    converted = convert_raw_tbl(raw_shipment_delivery)
    invalids = get_invalid_tbl(converted)
    cleaned = get_valid_tbl(converted)

    validation = tbl_validation(cleaned)
    if not validation:
        return {
            "status": "failed",
            "reason": "validation failed"
        }
    
    transformed = transform_tbl(cleaned)
    metrics = tbl_metrics(transformed)
    tree_output(invalids,cleaned,transformed)

    write_csv_file(output_invalids_path,invalids,invalid_columns,delimiter)
    write_csv_file(output_transformed_path,transformed,transformed_columns,delimiter)

    return {
        "status": "success",
        "metrics": metrics
    }

delivery_file_pipeline(input_path,",")