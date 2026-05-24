from src.validity_splitter import get_invalids_valids

def get_valids(raw_valids):
    return [
        {
            "inspection_id": unit.get("inspection_id"),
            "container_id": unit.get("container_id"),
            "vessel_name": unit.get("vessel_name"),
            "terminal": unit.get("terminal"),
            "cargo_type": unit.get("cargo_type"),
            "origin_country": unit.get("origin_country"),
            "weight_kg": unit.get("weight_kg"),
            "risk_score": unit.get("risk_score"),
            "inspection_minutes": unit.get("inspection_minutes"),
            "status": unit.get("status")
        }for unit in raw_valids
    ]