#generates valids and invalids table

from validator import validate_data

def split_invalids_valids(converted):

    invalids = []
    valids = []
    seen_ids = set()

    for po in converted:
        is_valid, reasons = validate_data(po)
        
        if not is_valid:
            discrepants = po.copy()
            discrepants["error_reasons"] = reasons
            invalids.append(discrepants)
            continue

        ids = po.get("order_id"),po.get("supplier_id")

        if ids in seen_ids:
            discrepants = po.copy()
            discrepants["error_reasons"] = "duplicate order_id & supplier_id"
            invalids.append(discrepants)
            continue

        seen_ids.add(ids)
        valids.append(po.copy())

    return invalids, valids

def duplicates_data(invalids):
    return [po for po in invalids if "duplicate" in po.get("error_reasons","").lower()]

