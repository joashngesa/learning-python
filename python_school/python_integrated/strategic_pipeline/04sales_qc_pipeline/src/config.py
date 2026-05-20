

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path (__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv (ENV_PATH)

def get_path(variable):
    path = os.getenv (variable)

    if path is None:
        raise ValueError (f"the variable {variable} is not found")
    
    return path

INPUT_PATH = BASE_DIR / get_path("INPUT_PATH")

FILE_COLUMNS = ["shipment_id","supplier_id","supplier_name","region",
                "product","category","unit_cost","quantity",
                "delivery_days","status"]

VALIDS_PATH = BASE_DIR / get_path ("VALIDS_PATH")
INVALIDS_PATH = BASE_DIR / get_path ("INVALIDS_PATH")
SUPPLIER_SUMMARY_PATH = BASE_DIR / get_path ("SUPPLIER_SUMMARY_PATH")
REGION_SUMMARY_PATH = BASE_DIR / get_path ("REGION_SUMMARY_PATH")

        