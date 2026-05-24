from src.validator import validate_date

def get_invalids_valids(converted):

    invalids = []
    raw_valids = []
    seen_ids = set()

    for unit in converted:
        is_valid, reasons = validate_date(unit)

        if not is_valid:
            invalid_data = unit.copy()
            invalid_data["error_reasons"] = reasons
            invalids.append (invalid_data)
            continue

        #duplicate keys = container_id, cargo_type and origin_country

        container_id = unit.get("container_id")
        cargo_type = unit.get("cargo_type")
        origin_country = unit.get("origin_country")
        keys = (container_id,cargo_type,origin_country)

        if keys in seen_ids:
            invalid_data = unit.copy()
            invalid_data["error_reasons"] = "duplicate container_id,cargo_type,origin_country"
            invalids.append (invalid_data)
            
        else:
            seen_ids.add (keys)
            raw_valids.append (unit.copy())

    return invalids, raw_valids
