records = [
    {"id": 1, "price": 100},
    {"price": 200},
    {"id": 3, "price": 300}
]
#every item must have "id"
#if one item is missing id → return False
#otherwise return True



#clean_data() returns valid rows
#validate_data() returns True/False
#calculate_metrics() returns a dictionary with:
#total_revenue
#valid_items

def clean_data(records):
    return [item for item in records if "id" in item]

def validate_data(scrubbed):
    for item in scrubbed:
        if "id" not in item:
            return False
        
    return True

def calc_metrics(scrubbed):
    revenue = 0
    for item in scrubbed:
        revenue += item.get("price",0)

    return {
        "Total_revenue": revenue,
        "Valid_items": len(scrubbed)
    }

scrubbed = clean_data(records)
validated = validate_data(scrubbed)

if validated:
    metrics = calc_metrics(scrubbed)
    print("pipeline executed!")
    print(metrics)
else:
    print("pipeline unsuccessful")