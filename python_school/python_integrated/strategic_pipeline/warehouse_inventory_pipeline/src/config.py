
#in the next lesson on modules, teach me more on how they interact with environments, help me understand the modules pathlib and dotenv and the concepts applied to code this, save this in memory for next lesson
#in the next lesson, enlighten me on when we are going to learn about class and objects (at what stage in the blue print will be doing this)
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)

def get_path(variable_name):
    path = os.getenv (variable_name)

    if path is None:
        raise ValueError (f"the path {variable_name} is not found")

    return path

INPUT_PATH = get_path ("INPUT_PATH")
RAW_COLUMNS = ["item_id","warehouse_id","warehouse_region","product_name","category","unit_cost","stock_qty","reorder_level","stock_status"]

VALIDS_PATH = get_path ("VALIDS_PATH")
INVALIDS_PATH = get_path ("INVALIDS_PATH")
DUPLICATES_PATH = get_path ("DUPLICATES_PATH")
TRANSFORMED_PATH = get_path ("TRANSFORMED_PATH")
SUMMARY_PATH = get_path ("SUMMARY_PATH")


VALIDS_COLUMN = ["item_id","warehouse_id","warehouse_region","product_name","category","unit_cost","stock_qty","reorder_level","stock_status"]
INVALIDS_COLUMN = ["item_id","warehouse_id","warehouse_region","product_name","category","unit_cost","stock_qty","reorder_level","stock_status","error_reasons"]
DUPLICATES_COLUMN =  ["item_id","warehouse_id","warehouse_region","product_name","category","unit_cost","stock_qty","reorder_level","stock_status","error_reasons"]
TRANSFORMED_COLUMN = ["item_id","warehouse_id","warehouse_region","product_name","category","inventory_value","reorder_flag"]
SUMMARY_COLUMN = ["warehouse_region","category","total_inventory_value","item_count","reorder_item_count"]