#expected output
# "inspection_id": "",
        #container_count
        #total_weight_kg
        #average_risk_score
        #average_inspection_minutes
        #held_count
        #rejected_count

def summarize_terminal_cargo(valids):

    summary = {}

    for unit in valids:
        
        container_id = unit.get("container_id")
        vessel_name = unit.get("vessel_name")
        terminal = unit.get("terminal")
        cargo_type = unit.get("cargo_type")
        origin_country = unit.get("origin_country")
        weight_kg = unit.get("weight_kg")
        risk_score = unit.get("risk_score")
        inspection_minutes = unit.get("inspection_minutes")
        status = unit.get("status")
        keys = (terminal, cargo_type)

        if keys not in summary:
            summary[keys] = {
                "container_count": 0,
                "total_weight_kg": 0,
                "average_risk_score": 0,
                "average_inspection_minutes": 0,
                "held_count": 0,
                "rejected_count": 0,
                "total_risk_score": 0,
                "total_inspec_min": 0
            }

        summary[keys]["container_count"] += 1
        summary[keys]["total_weight_kg"] += weight_kg
        summary[keys]["total_risk_score"] += risk_score
        summary[keys]["total_inspec_min"] += inspection_minutes
                
        
        if status == "Held":
                summary[keys]["held_count"] += 1
        elif status == "Rejected":
                summary[keys]["rejected_count"] += 1

    for field in summary:
        new = summary[field]
        new["average_risk_score"] = new["total_risk_score"] / new["container_count"]
        new["average_inspection_minutes"] = new["total_inspec_min"] / new["container_count"]

    return list (summary.values())