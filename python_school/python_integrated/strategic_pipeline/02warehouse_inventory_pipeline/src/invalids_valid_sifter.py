
from validate import data_validation

def sifter(converted):
    invalids = []
    valids = []
    seen_ids = set()

    for unit in converted:
        is_valid, reasons = data_validation(unit)

        if not is_valid:
            faulty_data = unit.copy()
            faulty_data["error_reasons"] = reasons
            invalids.append(faulty_data)
            continue

        ids = (unit.get("item_id"), unit.get("warehouse_id")) #i only changed the oder_id to item_id and the result stop working, whereas it worked before
        
        if ids in seen_ids:
            faulty_data = unit.copy()
            faulty_data["error_reasons"] = "item_id & warehouse_id duplicates"
            invalids.append(faulty_data)
            continue

        seen_ids.add(ids)
        valids.append(unit.copy())

    return invalids, valids 

def duplicate_data(invalids):
    return [unit for unit in invalids if "duplicate" in unit.get("error_reasons","").lower()]

