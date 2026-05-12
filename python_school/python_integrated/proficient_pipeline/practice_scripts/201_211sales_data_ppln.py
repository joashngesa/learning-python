                            #MINI SALES DATA PIPELINE
#🗺️pipeline map
    #read_raw_file()
    #parse_line()
    #parse_records()
    #is_valid_record()
    #separate_valid_invalid()
    #detect_duplicates()
    #group_by_region_category()
    #write_records_to_csv()
    #write_summary_to_csv()
    #main()

import os
import csv
from tabulate import tabulate

input_path = "c:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/source files/raw_sales.txt"

def read_txt_file_parse_data(file_path):

    persed_data = []
    try:
        with open (file_path, "r",encoding="utf-8",newline="") as file:
            next(file)

            for item in file:
                source = item.strip().split("|")

                if len(source) != 7:
                    continue

                order_id = source[0].strip()
                customer_id = source[1].strip()
                product = source[2].strip()
                region = source[3].strip()
                category = source[4].strip()
                price = source[5].strip()
                qty = source[6].strip()

                raw = {
                    "order_id": order_id,
                    "customer_id": customer_id,
                    "product": product,
                    "region": region,
                    "category": category,
                    "price": price,
                    "qty": qty
                }

                persed_data.append(raw)
    
    except Exception as e:
        print(f"error occurred: {e}")
        return []

    
    return persed_data

            #parsed = read_txt_file_parse_data(input_path)
            #print(tabulate(parsed,headers="keys",tablefmt="grid"))

def convert_data(parsed):
    converted = []
    for item in parsed:
        cnv = item.copy()

        try:
            cnv["price"] = int(cnv["price"]) if cnv["price"] != "" else None
        except ValueError:
            cnv["price"] = None
    
        try:
            cnv["qty"] = int(cnv["qty"]) if cnv["qty"] != "" else None
        except ValueError:
            cnv["qty"] = None

        converted.append(cnv)

    return converted

            #converted = convert_data(parsed)
            #print(tabulate(converted,headers="keys",tablefmt="grid"))

#validation rules
    #order_id is missing
    #customer_id is missing
    #product is missing
    #region is missing
    #category is missing
    #price is missing
    #qty is missing
    #price is not a valid number
    #qty is not a valid number
    #price <= 0
    #qty <= 0

def data_validation(item):
    tbl_columns = ["order_id","customer_id","product","region","category","price","qty"]

    for column in tbl_columns:
        if column not in item:
            return False, f"the column {column} is missing"
        
    order_id = item.get("order_id")
    customer_id = item.get("customer_id")
    product = item.get("product")
    region = item.get("region")
    category = item.get("category")
    price = item.get("price")
    qty = item.get("qty")

    if not isinstance (order_id,str) or order_id == "":
        return False, "the order_id needs to be a non_empty string"
    if not isinstance (customer_id,str) or customer_id == "":
        return False, "the customer_id needs to be a non_empty string"
    if not isinstance (product,str) or product == "":
        return False, "the product needs to be a non empty string"
    if not isinstance (region,str) or region == "":
        return False, "the region needs to be non empty string"
    if not isinstance (category,str) or category == "":
        return False, "category needs to be non_empty string"
    if not isinstance (price,(int,float)):
        return False, "the price needs to be a non_empty number"
    if not isinstance (qty,int):
        return False, "quantity needs to be a non_empty number"
    if price <= 0:
        return False, "the price should be greater than zero"
    if qty <= 0:
        return False, "the quantity should be greater than zero"
    

    return True, None

#duplicate logic -_-__  only valid items should be checked for duplicate
    #order_id + customer_id

def split_valid_invalids(converted):
    valids = []
    invalids = []
    seen_ids = set()

    for item in converted:
        is_valid, reasons = data_validation(item)

        if not is_valid:
            invalid_rows = item.copy()
            invalid_rows["error_reasons"] = reasons
            invalids.append(invalid_rows)

            continue

        ids = item.get("order_id"),item.get("customer_id")

        if ids in seen_ids:
            invalid_rows =item.copy()
            invalid_rows["error_reasons"] = "duplicate order_id & customer_id"  
            invalids.append(invalid_rows)

            continue

        seen_ids.add(ids)
        valids.append(item.copy())

    return valids, invalids
    
            #valids, invalids = split_valid_invalids(converted)
            #print(tabulate(invalids,headers="keys",tablefmt="grid"))
            #print(tabulate(valids,headers="keys",tablefmt="grid")) 

def duplicate_sales(invalids):
    return [item for item in invalids if "duplicate" in str (item.get("error_reasons").lower())]

            #duplicates = duplicate_sales(invalids)
            #print(tabulate(duplicates,headers="keys",tablefmt="grid")) 

def revenue_calc(item):
    return item.get("price") * item.get("qty")

def transformed_data(valids):
    return [
        {
            "order_id": item.get("order_id"),
            "customer_id": item.get("customer_id"),
            "product": item.get("product"),
            "region": item.get("region"),
            "category": item.get("category"),
            "revenue": revenue_calc(item)
        }
        for item in valids
    ]

            #transformed = transformed_data(valids)
            #print(tabulate(transformed,headers="keys",tablefmt="grid")) 

#total revenue grouped by region and category

def revenue_region_category_summary(transformed):
    summary = {}
    for item in transformed:
        revenue = item.get("revenue")
        region = item.get("region")
        category = item.get("category")
        group = (region, category)

        if group not in summary:
            summary[group] = revenue
        else:
            summary[group] += revenue

    revenue_summary = []

    for group, tot_revenue in summary.items():
        region, category = group
        revenue_summary.append(
            {
                "region": region,
                "category": category,
                "total revenue": tot_revenue
            }
        )
        
    return revenue_summary

            #summary_rev = revenue_region_category_summary(transformed)
            #print(tabulate(summary_rev,headers="keys",tablefmt="grid")) 

#write csv outputs
    #clean_sales.csv
    #invalid_sales.csv
    #duplicate_sales.csv
    #region_category_summary.csv


def write_output_csv(output_path,data,output_delimiter,output_columns):
    folder_path = os.path.dirname (output_path)

    if folder_path :
        os.makedirs (folder_path,exist_ok=True)

    with open (output_path, "w", newline="") as file:
        writer = csv.DictWriter (file, delimiter=output_delimiter, fieldnames=output_columns,extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)
        print("write to: ",os.path.abspath(output_path))

#final output on the console:
#Pipeline completed.
#...
#Total raw rows: 12
#Valid records: X
#Invalid records: X
#Unique clean records: X   --every row entails a record which is unique, help me understand the difference between this and len(valids)
#Duplicate records: X
#...
#Files written:
#clean_sales.csv
#invalid_sales.csv
#duplicate_sales.csv
#region_category_summary.csv

def output_print(parsed_data,valids,invalids,duplicates,summary_rev):
    print("Pipeline completed\n")
    print("Total raw rows: ",len(parsed_data))
    print("\nValid records: ",len(valids))
    print("\nInvalid records ",len(invalids))
    print("\nDuplicate records", len(duplicates))
    print("\nclean sales")
    print(tabulate(valids, headers="keys", tablefmt="grid"))
    print("\ninvalid sales")
    print(tabulate(invalids, headers="keys", tablefmt="grid"))
    print("\nduplicate sales")
    print(tabulate(duplicates, headers="keys",tablefmt="grid"))
    print("\nregion_category summary")
    print(tabulate(summary_rev, headers="keys", tablefmt="grid"))

valids_path = "c:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/mini_sales_pipeline/clean_sales.csv"
invalids_path = "c:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/mini_sales_pipeline/invalid_sales.csv"
duplicates_path = "c:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/mini_sales_pipeline/duplicates_sales.csv"
summary_path = "c:/guru_g/data_engineer/learning/python/python_school/python_integrated/proficient_pipeline/practice_files/worked_on_files/mini_sales_pipeline/revenue_summary.csv"

valids_columns = ["order_id","customer_id","product","region","category","price","qty"]
invalids_columns = ["order_id","customer_id","product","region","category","price","qty","error_reasons"]
duplicates_columns = ["order_id","customer_id","product","region","category","price","qty","error_reasons"]
summary_columns = ["region","category","total revenue"]

def exec_read_write_sales_pipeline(file_path,output_delimiter):
   parsed = read_txt_file_parse_data(file_path) 
   converted = convert_data(parsed)

   if not converted:
       return {
           "status": "failed",
           "reason": "conversion failed"
       }
   
   valids, invalids = split_valid_invalids(converted)
   duplicates = duplicate_sales(invalids)
   transformed = transformed_data(valids)
   summary_rev = revenue_region_category_summary(transformed)
   write_output_csv(valids_path,valids,output_delimiter,valids_columns)
   write_output_csv(invalids_path,invalids,output_delimiter,invalids_columns)
   write_output_csv(duplicates_path,duplicates,output_delimiter,duplicates_columns)
   write_output_csv(summary_path,summary_rev,output_delimiter,summary_columns)
   output_print(parsed,valids,invalids,duplicates,summary_rev)

   return {
       "status": "pipeline success",
       "transformed data": transformed
   }


exec_read_write_sales_pipeline(input_path,"|")