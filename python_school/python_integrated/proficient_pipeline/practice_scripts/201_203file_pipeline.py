#SUPPLY CHAIN ORDERS

import csv
from tabulate import tabulate

def execute_file_pipeline(filepath,TITLE,delimiter):
    
    #Function that reads file from source path
    def read_csv_file(filepath,delimiter):
        try:
            with open (filepath,"r",newline = "") as file:
                reader = csv.DictReader (file,delimiter = delimiter)
                return list(reader)
                
        except FileNotFoundError:
            print(f"the {filepath} is not found, kindly confirm the data source or recheck file path)")
            return []
        
    raw_supplier_orders = read_csv_file(filepath,delimiter)

    #after inspecting the raw files, we need to convert strings to integer and float data types
    def convert_data_types(raw_supplier_orders):
        converted_data = []

        for unit in raw_supplier_orders:
            new_data = unit.copy()
            try:
                new_data["order_id"] = int(new_data["order_id"]) if new_data["order_id"] != "" else None
                new_data["price"] = float(new_data["price"]) if new_data["price"] != "" else None
                new_data["qty"] = int(new_data["qty"]) if new_data["qty"] != "" else None
            except:
                new_data["order_id"] = None
                new_data["price"] = None
                new_data["qty"] = None

            converted_data.append(new_data)

        return converted_data
    
    converted = convert_data_types(raw_supplier_orders)

    def supplier_orders_pipeline(TITLE,converted):

        def is_valid_tbl(unit):
            if not all (keys in unit for keys in ["order_id","product","price","qty"]):
                return False
            order_id = unit.get("order_id")
            price = unit.get("price")
            qty = unit.get("qty")
                     
            if not isinstance (order_id,int):
                return False
            if not isinstance (price,(int,float)):
                return False
            if not isinstance (qty,int):
                return False
            if price <= 0 or qty <= 0:
                return False
                            
            return True
        
        def invalid_data(converted):
            return [unit for unit in converted if not is_valid_tbl(unit)]
        
        invalids = invalid_data(converted)

        def clean_data(converted):
            return [unit for unit in converted if is_valid_tbl(unit)]
        
        cleaned = clean_data(converted)
        
        def tbl_validation(cleaned):
            for unit in cleaned:
                if not is_valid_tbl(unit):
                    return False
                
            return True
        
        validation = tbl_validation(cleaned)

        def revenue_calc(unit):
            return unit.get("price") * unit.get("qty")
        
        #Classification rules
        #revenue > 1000 → "high_value"
        #revenue > 300 → "medium_value"
        #else → "low_value"
        def revenue_classifier(unit):
            revenue = revenue_calc(unit)

            if revenue > 1000:
                return "high_value"
            elif revenue > 300:
                return "medium value"
            else:
                return "low_value"
            
        def tbl_transformation(cleaned):
            return [
                {
                    "order_id": unit.get("order_id"),
                    "product": unit.get("product"),
                    "revenue": revenue_calc(unit),
                    "category": revenue_classifier(unit)
                }
                for unit in cleaned
            ]
        
        transformed = tbl_transformation(cleaned)

        def high_value_orders(transformed):
            return sum (1 for unit in transformed if unit.get("category") == "high_value")

        #metrics needed:
            #total orders
            #total revenue
            #high value orders
        def tbl_metrics(transformed):
            total_revenue = 0

            for unit in transformed:
                total_revenue += unit.get("revenue")

            return {
                "total orders": len(transformed),
                "total revenue": total_revenue,
                "high value orders": high_value_orders(transformed)
            }
        
        metrics = tbl_metrics(transformed)

        def print_tbl(TITLE,invalids,cleaned,transformed):
            print(f"{TITLE}")
            print("\nInvalid data")
            print(tabulate(invalids, headers = "keys", tablefmt = "grid"))
            print("\nCleaned data")
            print(tabulate(cleaned, headers = "keys", tablefmt = "grid"))
            print("\nTransformed data")
            print(tabulate(transformed, headers = "keys", tablefmt = "grid"))

          #invalid data:
        #"status": "failed",
        #"reason": "validation failed"

        if not validation:
            output = {
                "status": "pipeline failed.",
                "reason": "validation failed"
            }
            print(output)
            return output
        
        output = {
            "status": "success",
            "invalid table": invalids,
            "transformed table": transformed,
            "table metrics": metrics
        }

        print("status: success")
        print("table metrics",metrics)
        print_tbl(TITLE,invalids,cleaned,transformed)
        return output
    
    output = supplier_orders_pipeline(TITLE,converted)
                    
    

        #inv_columns = ["order_id","product","price","qty"]
        #trf_columns = ["order_id","product","revenue","category"]

    def write_csv_invalids(filepath,data,column_names,delimiter = ";"):
        with open (filepath,"w",newline="") as file:
            writer = csv.DictWriter (file,fieldnames=column_names,delimiter=delimiter)
            writer.writeheader()
            writer.writerows(data)

    if output.get("status") == "success":
        write_csv_invalids("pct101_invalid_tbl",output["invalid table"],["order_id","product","price","qty"],delimiter = delimiter) 
        write_csv_invalids("pct101_transformed_tbl",output["transformed table"],["order_id","product","revenue","category"],delimiter = delimiter)   

    return output


execute_file_pipeline("../source_files/pct101_supplier_orders.csv","SUPPLIER ORDERS",";")




