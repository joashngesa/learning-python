#FOR EDUCATIONAL PURPOSES ONLY:

def validate_record_without_duplicates(unit):
    required_fields = ["order_id", "product", "price", "qty", "file_source"]

    for field in required_fields:
        if field not in unit:
            return False, f"missing field: {field}"

    order_id = unit.get("order_id")
    product = unit.get("product")
    price = unit.get("price")
    qty = unit.get("qty")
    file_source = unit.get("file_source")

    if not isinstance(order_id, int):
        return False, "order_id must be integer"

    if not isinstance(product, str) or product.strip() == "":
        return False, "product must be non-empty text"

    if not isinstance(price, int):
        return False, "price must be integer"

    if not isinstance(qty, int):
        return False, "qty must be integer"

    if price <= 0:
        return False, "price must be greater than 0"

    if qty <= 0:
        return False, "qty must be greater than 0"

    if not isinstance(file_source, str) or file_source.strip() == "":
        return False, "file_source must be non-empty text"

    return True, "valid"


def split_valid_invalid_records(merged):
    valids = []
    invalids = []
    seen_order_ids = set()

    for unit in merged:
        is_valid, reason = validate_record_without_duplicates(unit)

        if not is_valid:
            invalid_unit = unit.copy()
            invalid_unit["error_reason"] = reason
            invalids.append(invalid_unit)
            continue

        order_id = unit.get("order_id")

        if order_id in seen_order_ids:
            invalid_unit = unit.copy()
            invalid_unit["error_reason"] = "duplicate order_id"
            invalids.append(invalid_unit)
            continue

        seen_order_ids.add(order_id)
        valids.append(unit)

    return valids, invalids


def summarize_errors(invalids):
    error_summary = {}

    for unit in invalids:
        reason = unit.get("error_reason")

        if reason not in error_summary:
            error_summary[reason] = 1
        else:
            error_summary[reason] += 1

    return error_summary


def data_quality_report(merged, valids, invalids):
    total_records = len(merged)
    valid_records = len(valids)
    invalid_records = len(invalids)

    if total_records == 0:
        valid_percentage = 0
        invalid_percentage = 0
    else:
        valid_percentage = round((valid_records / total_records) * 100, 2)
        invalid_percentage = round((invalid_records / total_records) * 100, 2)

    return {
        "total_records": total_records,
        "valid_records": valid_records,
        "invalid_records": invalid_records,
        "valid_percentage": valid_percentage,
        "invalid_percentage": invalid_percentage,
        "error_summary": summarize_errors(invalids)
    }






#test experiment

import csv

def read_csv_file(file_path, delimiter):
    try:
        records = []

        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file, delimiter=delimiter)

            for row in reader:
                # TODO:
                # 1. Strip all fields
                # 2. Skip rows with missing order_id
                # 3. Convert amount to float

                records.append(row)

        return records

    except FileNotFoundError:
        return None