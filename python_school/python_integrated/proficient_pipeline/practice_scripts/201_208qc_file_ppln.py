                            #CUSTOMER TRANSACTION QUALITY PIPELINE
#Transaction pipeline goal:
#1. raw data
#2. convert_transactions()▶️
#3. validate one record ▶️
#4. split valid/invalid ▶️▶️
#5. transform ▶️
#6. metrics ▶️
#7. quality report ▶️ 
#8. run pipeline

#qualitiy check successfully coded
#


import os
import csv
from tabulate import tabulate

raw_transactions = [
    {"transaction_id": "T1001", "customer_id": "C001", "amount": "250", "status": "completed", "channel": "web"},
    {"transaction_id": "T1002", "customer_id": "C002", "amount": "-40", "status": "completed", "channel": "store"},
    {"transaction_id": "T1003", "customer_id": "", "amount": "120", "status": "completed", "channel": "web"},
    {"transaction_id": "T1004", "customer_id": "C004", "amount": "abc", "status": "completed", "channel": "mobile"},
    {"transaction_id": "T1005", "customer_id": "C005", "amount": "600", "status": "pending", "channel": "web"},
    {"transaction_id": "T1001", "customer_id": "C006", "amount": "700", "status": "completed", "channel": "store"},
    {"transaction_id": "T1007", "customer_id": "C007", "amount": "1000", "status": "completed", "channel": "mobile"},
]
                    #print(tabulate(raw_transactions, headers="keys", tablefmt="grid"))

#Each record should have:
    #transaction_id
    #customer_id
    #amount
    #status
    #channel

#Conversion rules
    #convert amount to integer
    #if conversion fails, set amount to None
def convert_data(file):
    converted_tbl = []
    for txn in file:
        cnv_data = txn.copy()
        try:
            cnv_data["amount"] = int(txn["amount"]) if txn["amount"] != "" else None 

        except ValueError:
            cnv_data["amount"] = None

        converted_tbl.append(cnv_data)

    return converted_tbl
print("[INFO] conversion complete")
                    #converted = convert_data(raw_transactions)
                    #print(tabulate(converted, headers="keys", tablefmt="grid"))

#validation rules
    #transaction_id must be non-empty string
    #customer_id must be non-empty string
    #amount must be integer
    #amount must be greater than 0
    #status must be "completed"
    #channel must be one of: "web", "store", "mobile"
def validate_data(txn):
    required_columns = ["transaction_id","customer_id","amount","channel","status"]
    for column in required_columns:
        if column not in txn:
            return False, f"missing field: {column}"
        
    txn_id = txn.get("transaction_id")
    customer_id = txn.get("customer_id")
    amount = txn.get("amount")
    status = txn.get("status")
    channel = txn.get("channel")
    allowed_channels = ["web","mobile","store"]

    if not isinstance (txn_id,str) or txn_id.strip() == "":
        return False, "txn_id needs to be a non_empty string"
    if not isinstance (customer_id,str) or customer_id.strip() == "":
        return False, "customer_id needs to be a non_empty string"
    if not isinstance (amount,int):
        return False, "amount must be integer"
    if amount <= 0:
        return False, "amount must be greater than zero"
    if status != "completed":
        return False, "only completed transactions are recorded"
    if channel not in allowed_channels:
        return False, "channel must be one of web,store,mobile"

    return True, "valid"                       
    
print("[INFO] validation complete")

#when creating spli invalid_valid function:
    #use seen_transaction_ids = set()
    #keep first occurrence
    #reject duplicate transaction IDs
    #invalid records must include error_reason

def split_invalid_valid_tbls(converted):
    invalids = []
    valids = []
    seen_txn_id = set()

    for txn  in converted:
        is_valid, reasons = validate_data(txn)

        if not is_valid:
            invalid_data = txn.copy()
            invalid_data["error_reason"] = reasons
            invalids.append(invalid_data)
            continue

        txn_id = txn.get("transaction_id")

        if txn_id in seen_txn_id:
            invalid_data = txn.copy()
            invalid_data["error_reason"] = "duplicate_order_id"
            invalids.append(invalid_data)
            continue

        seen_txn_id.add(txn_id)
        valids.append(txn)

    return invalids,valids,seen_txn_id

                    #invalids,valids =split_invalid_invalid_tbls(converted)
                    #print(tabulate(invalids, headers="keys", tablefmt="grid"))
                    #print(tabulate(valids, headers="keys", tablefmt="grid"))
#transform data to:
    #transaction_id
    #customer_id
    #amount
    #channel
    #amount_category

#category rules
    #amount >= 500 → "high"
    #amount >= 200 → "medium"
    #else → "low"
def grouping_amount(txn):
    amount = txn.get("amount")

    if amount >= 500:
        return "high"
    if amount >= 200:
        return "medium"
    else:
        return "low"
    
def transform_data(valids):
    return [{
        "txn_id": txn.get("transaction_id"),
        "customer_id": txn.get("customer_id"),
        "amount": txn.get("amount"),
        "channel": txn.get("channel"),
        "amount_category": grouping_amount(txn)
    }for txn in valids
    ]

                    #transformed = transform_data(valids)
                    #print(tabulate(transformed, headers="keys", tablefmt="grid"))

def high_value_txns(transformed):
    return sum([1 for txn in transformed if txn.get("amount_category") == "high"])

#transaction metrics
    #"total_completed_transactions": ...,
    #"total_amount": ...,
    #"high_value_transactions": ...

def data_metrics(transformed):
    tot_amount = 0

    for txn in transformed:
        tot_amount += txn.get("amount")

    return {
        "Total completed transactions": len(transformed),
        "total amount": tot_amount,
        "high value transactions": high_value_txns(transformed)
    }
                    #metrics = data_metrics(transformed)
                    #print(metrics)

#summarized trasaction errors
    #"total_records": ...,
    #"valid_records": ...,
    #"invalid_records": ...,
    #"valid_percentage": ...,
    #"invalid_percentage": ...,
    #"error_summary": ...

def error_summary(invalids):
    error_digest = {}

    for txn in invalids:
        reason = txn.get("error_reason")

        if reason not in error_digest:
            error_digest[reason] = 1
        else:
            error_digest[reason] += 1

    return error_digest   

                    #summary = error_summary(invalids)
                    #print(summary)

def quality_report(converted,invalids,valids):
    total_records = len(converted)
    valid_records = len(valids)
    invalid_records = len(invalids)

    if total_records == 0:
        valid_pcnt = 0
        invalid_pcnt = 0

    else:
        valid_pcnt = round((valid_records / total_records) * 100,2)
        invalid_pcnt = round((invalid_records / total_records) * 100,2)

    return {
        "Total records": total_records,
        "valid records": valid_records,
        "invalid records": invalid_records,
        "valid percentage": valid_pcnt,
        "invalid percentage": invalid_pcnt,
        "error summary": error_summary(invalids)
    }


def show_output(converted,seen_txn_id,invalids,valids,metrics):
    print("\nduplicate data")
    print(seen_txn_id)
    print("\ninvalid table")
    print(tabulate(invalids, headers="keys", tablefmt="grid"))
    print("\nvalid tables")
    print(tabulate(valids, headers="keys", tablefmt="grid"))
    print("\ndata metrics")
    print(metrics)
    print("\n error summary")
    print(quality_report(converted,invalids,valids)["error summary"])
        
def exec_qc_pipeline(file):
    converted = convert_data(file)
    invalids,valids,seen_txn_id =split_invalid_valid_tbls(converted)
    transformed = transform_data(valids)
    metrics = data_metrics(transformed)
    show_output(converted,seen_txn_id,invalids,valids,metrics)
    quality = quality_report(converted,invalids,valids)
    print("\nquality synpsis")
    print(quality)
    return {
        "status": "success",
        "data metrics": metrics,
        "quality report": quality
    }

exec_qc_pipeline(raw_transactions)