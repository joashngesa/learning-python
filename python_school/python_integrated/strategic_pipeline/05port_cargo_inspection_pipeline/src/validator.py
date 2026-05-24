
#numeric rules
    #weight_kg must exist and be greater than 0
    #risk_score must exist and be between 1 and 100
    #inspection_minutes must exist and be greater than 0
#allowed terminals
    #["Terminal A", "Terminal B", "Terminal C", "Terminal D"]
#allowed_cargo_types
    #["Electronics", "Food", "Chemicals", "Textiles", "Machinery", "Furniture"]
#allowed status
    #["Cleared", "Held", "Rejected", "Pending"]

data_fields = ["inspection_id","container_id","vessel_name",
               "terminal","cargo_type","origin_country",
               "weight_kg","risk_score","inspection_minutes"
               ,"status"]

allowed_terminals = ["Terminal A", "Terminal B", "Terminal C", "Terminal D"]
allowed_cargo_types = ["Electronics", "Food", "Chemicals", "Textiles", "Machinery", "Furniture"]
allowed_status = ["Cleared", "Held", "Rejected", "Pending"]

def validate_date (unit):

    error_reasons = unit.get("error_reasons")
    if error_reasons:
        return False, "parse error"
    
    for column in data_fields:
        if column not in unit:
            return False, f"the column {column}is missing"
        
    inspection_id = unit.get("inspection_id")
    container_id = unit.get("container_id")
    vessel_name = unit.get("vessel_name")
    terminal = unit.get("terminal")
    cargo_type = unit.get("cargo_type")
    origin_country = unit.get("origin_country")
    weight_kg = unit.get("weight_kg")
    risk_score = unit.get("risk_score")
    inspection_minutes = unit.get("inspection_minutes")
    status = unit.get("status")

    if inspection_id is None:
        return False, f"inspection_id is missing from the data"
    if not isinstance (inspection_id,str):
        return False, "inspection_id should be a string"
    if not inspection_id.strip():
        return False, "inspection_id is blank"
    if container_id is None:
        return False, "container_id is missing from theb data"
    if not isinstance (container_id,str):
        return False, "container_id should be a string"
    if not container_id.strip():
        return False, "container_id is blank"
    if vessel_name is None:
        return False, f"vessel_name is missing from the data"
    if not isinstance (vessel_name,str):
        return False, "vessel_name should be a string"
    if not vessel_name.strip():
        return False, "vessel_name is blank"
    if terminal not in allowed_terminals:
        return False, "terminal must be one of terminal A,B,C,D "
    if terminal is None:
        return False, "terminal is missing"
    if not isinstance (terminal,str):
        return False, "terminal should be a string"
    if not terminal.strip():
        return False, "terminal is blank"
    if cargo_type not in allowed_cargo_types:
        return False, "cargo_types must be one of electronics,food,chemicals,textiles,machinery,furniture"
    if cargo_type is None:
        return False, "cargo_type is missing from the data"
    if not cargo_type.strip():
        return False, "cargo_type is blank"
    if origin_country is None:
        return False, "origin_country is missing from the data"
    if not origin_country.strip():
        return False, "origin_country is blank"
    if weight_kg is None:
        return False, "weight_kg is missing from the data"
    if weight_kg <= 0:
        return False, "weight_kg should be greater than zero"
    if risk_score is None:
        return False, "risk_score is missing from the data"
    if not isinstance (risk_score,int):
        return False, "risk_score is not integer"
    if not (1 <= risk_score <= 100):
        return False, "risk score should be between 1 and 100"
    if inspection_minutes is None:
        return False, "inspection_minutes is missing from the data"
    if not isinstance (inspection_minutes,int):
        return False, "inspection_minutes should be integer"
    if inspection_minutes <= 0:
        return False, "inspection_minutes should be greater than zero"
    if status is None:
        return False, "status is not found in data"
    if status not in allowed_status:
        return False, "status must be one of Cleared,Held,Rejected,Pending"
    
    return True, None

    