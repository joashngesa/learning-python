#ingest data from raw file folder

def read_data(file_path):
    
    parsed = []

    try:
        with open (file_path, "r", newline="",encoding="utf-8") as file:
            next(file)

            for unit in file:
                stock = unit.strip().split("|")

                if len(stock) != 9:
                    continue

                item_id = stock[0].strip()
                warehouse_id = stock[1].strip()
                warehouse_region = stock[2].strip()
                product_name = stock[3].strip()
                category = stock[4].strip()
                unit_cost = stock[5].strip()
                stock_qty = stock[6].strip()
                reorder_level = stock[7].strip()
                stock_status = stock[8].strip()

               

                raw = {
                    "item_id": item_id,
                    "warehouse_id": warehouse_id,
                    "warehouse_region": warehouse_region,
                    "product_name": product_name,
                    "category": category,
                    "unit_cost": unit_cost,
                    "stock_qty": stock_qty,
                    "reorder_level": reorder_level,
                    "stock_status": stock_status
                }

                parsed.append(raw)

    except Exception as e:
        print(f"Error: {e}")
        return []


    return parsed

