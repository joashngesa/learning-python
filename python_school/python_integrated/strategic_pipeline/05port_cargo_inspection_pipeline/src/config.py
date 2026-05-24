import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_VAR = BASE_DIR / ".env"

load_dotenv(ENV_VAR)

def get_path(variable_name):
    path = os.getenv(variable_name)

    if not path:
        raise ValueError(f"Error: {variable_name} variable not found")
    
    return path

INPUT_PATH = get_path("INPUT_PATH")
VALIDS_PATH = get_path("VALIDS_PATH")
INVALIDS_PATH = get_path("INVALIDS_PATH")
SUMMARY_PATH = get_path("SUMMARY_PATH")
HIGH_RISK_PATH = get_path("HIGH_RISK_PATH")