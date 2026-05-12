#shippinng status
shipments = [
    {"id": 1, "days": 3},
    {"id": 2, "days": 7},
    {"id": 3, "days": 10}
]
#create helper function
#days <= 5 → "on_time"
#days <= 8 → "delayed"
#else → "late"

def classify_shipping(shpt):
   
        if shpt.get("days") <= 5:
            return "on_time"
        elif shpt.get("days") <= 8:
            return "delayed"
        else:
            return "late"
    

def status_check(shipments):
    return [
        {
            "id": shpt.get("id"),
            "status": classify_shipping(shpt)
        }
        for shpt in shipments
    ]

metrics = status_check(shipments)
print("Metrics: ",metrics)