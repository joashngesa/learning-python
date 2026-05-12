#PROCUREMENT LEAD TEAM
suppliers = [
    {"supplier": "A", "lead_time": 3},
    {"supplier": "B", "lead_time": 8},
    {"supplier": "C", "lead_time": 15}
]
#Build functions; def classify_supplier(item),transform_suppliers(data)
#lead_time <= 5 → "fast"
#lead_time <= 10 → "moderate"
#else → "slow"

from tabulate import tabulate

def supplier_classifier(supp):
    if supp.get("lead_time") <= 5:
        return "fast"
    elif supp.get("lead_time") <= 10:
        return "moderate"
    else:
        return "slow"
    
def transform_suppliers(suppliers):
    return [
        {
            "supplier": supp.get("supplier"),
            "lead_time": supp.get("lead_time"),
            "speed": supplier_classifier(supp)
        }
        for supp in suppliers
    ]

transformed = transform_suppliers(suppliers)
print(tabulate(transformed, headers = "keys", tablefmt = "grid"))