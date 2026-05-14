
import os
from dotenv import load_dotenv

load_dotenv()

INPUT_PATH = os.getenv ("INPUT_PATH")
OUTPUT_DIR = os.getenv ("OUTPUT_DIR")

INVALIDS_PATH = os.path.join (OUTPUT_DIR, "invalids_sales.csv")
VALIDS_PATH = os.path.join (OUTPUT_DIR, "valid_sales.csv")
DUPLICATES_PATH = os.path.join (OUTPUT_DIR, "duplicates_sales.csv")
SUMMARY_PATH = os.path.join (OUTPUT_DIR,"sales_summary.csv")

FILE_COLUMNS = ["order_id","supplier_id","supplier_name","category","region","unit_cost","quantity","order_status"]
ALLOWED_ORDER_STATUS = ["delivered","pending","cancelled","returned"]

INVALIDS_COLUMNS = ["order_id","supplier_id","supplier_name","category","region","unit_cost","quantity","order_status","error_reasons"]
VALIDS_COLUMNS = ["order_id","supplier_id","supplier_name","category","region","unit_cost","quantity","order_status"]
DUPLICATES_COLUMNS =  ["order_id","supplier_id","supplier_name","category","region","unit_cost","quantity","order_status","error_reasons"]
SUMMARY_COLUMNS = ["supplier_name","category","total_cost","order_count"]

required_env_files = {
    "INPUT_PATH": INPUT_PATH,
    "INVALIDS_PATH": INVALIDS_PATH,
    "VALIDS_PATH": VALIDS_PATH,
    "DUPLICATES_PATH": DUPLICATES_PATH,
    "SUMMARY_PATH": SUMMARY_PATH
}

for path, value in required_env_files.items():
    if value is None or value == "":
        raise ValueError(f"{path} is missing from .env")