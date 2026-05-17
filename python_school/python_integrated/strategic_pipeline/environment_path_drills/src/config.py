
from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path (__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)

def get_path(variable_name):
    path = os.getenv (variable_name)

    if path is None:
        raise ValueError (f"{variable_name} was not found")
    
    return path

INPUT_PATH = BASE_DIR / get_path("INPUT_PATH")
OUTPUT_PATH = BASE_DIR / get_path("OUTPUT_PATH")


print("BASE_DIR:", BASE_DIR)
print("ENV_PATH:", ENV_PATH)
print("ENV exists:", ENV_PATH.exists())
print("INPUT_PATH:", INPUT_PATH)
print("INPUT exists:", INPUT_PATH.exists())
print("OUTPUT_PATH:", OUTPUT_PATH)