#Inventory value + risk flag
inventory = [
    {"sku": "A", "units": 10, "cost": 20},
    {"sku": "B", "units": 2, "cost": 500},
    {"sku": "C", "units": 50, "cost": 5}
]

from tabulate import tabulate

#calculate total value
def total_value(piece):
    return  piece.get("units") * piece.get("cost")
    
#value > 1000 → "high_risk"
#else → "normal"
def risk_flag(piece):
     value = piece.get("units") * piece.get("cost")
     if value > 1000:
          return "high_risk"
     else:
          return "normal"
     
def inventory_metrics(inventory):
     return [
          {
               "sku": piece.get("sku"),
               "value": total_value(piece),
               "risk": risk_flag(piece)
          }
          for piece in inventory
     ]

inventory_results = inventory_metrics(inventory)
print(tabulate(inventory_results, headers = "keys", tablefmt = "grid"))
