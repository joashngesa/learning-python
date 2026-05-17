#Read files from the data/raw folder

import os

def read_file(file_path):

    persed_data = []
    try:

        with open (file_path, "r", newline="",encoding="utf-8")as file:
            next(file)

            for po in file:
                txn = po.strip().split("|")

                if len(txn)!= 8:
                    continue

                order_id = txn[0].strip()
                supplier_id = txn[1].strip()
                supplier_name = txn[2].strip()
                category = txn[3].strip()
                region = txn[4].strip()
                unit_cost = txn[5].strip()
                quantity = txn[6].strip()
                order_status = txn[7].strip()

                raw = {
                    "order_id": order_id,
                    "supplier_id": supplier_id,
                    "supplier_name": supplier_name,
                    "category": category,
                    "region": region,
                    "unit_cost": unit_cost,
                    "quantity": quantity,
                    "order_status": order_status
                }

                persed_data.append(raw)

    except Exception as e:
        print(f"Error: {e}")
        return []
    

    return persed_data


