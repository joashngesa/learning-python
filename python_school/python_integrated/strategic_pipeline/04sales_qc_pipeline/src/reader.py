def read_file(file_path):
    
    persed = []
    try:
        with open (file_path, "r", newline="", encoding="utf-8-sig") as file:
            next (file)

            for stock in file:
                raw = stock.strip().split("|")

                if len (raw) != 10:
                    persed.append ({
                    "shipment_id": "",
                    "supplier_id": "",
                    "supplier_name": "",
                    "region": "",
                    "product": "",
                    "category": "",
                    "unit_cost": "",
                    "quantity": "",
                    "delivery_days": "",
                    "status": "",
                    "error_reasons": "the row does not have exactly 10 fields",
                    "extra_fields": ""
                    })
                    continue
                
                shipment_id= raw[0].strip()
                supplier_id= raw[1].strip()
                supplier_name = raw[2].strip()
                region = raw[3].strip()
                product = raw[4].strip()
                category = raw[5].strip()
                unit_cost = raw[6].strip()
                quantity = raw[7].strip()
                delivery_days = raw[8].strip()
                status = raw[9].strip()

                raw_data = {
                    "shipment_id":shipment_id,
                    "supplier_id": supplier_id,
                    "supplier_name": supplier_name,
                    "region": region,
                    "product": product,
                    "category": category,
                    "unit_cost": unit_cost,
                    "quantity": quantity,
                    "delivery_days": delivery_days,
                    "status": status,
                    "error_reasons": "",
                    "extra_fields": ""
                }

                persed.append (raw_data)

    except Exception as e:
        print (f"File read error: {e}")
        return []
    

    return persed
