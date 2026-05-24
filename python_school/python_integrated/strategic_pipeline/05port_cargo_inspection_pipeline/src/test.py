import os
from tabulate import tabulate

from config import INPUT_PATH
from reader import read_data
from cleaner import clean_data
from converter import convert_data
from validity_splitter import get_invalids_valids
from valids import get_valids
from terminal_aggregator import summarize_terminal_cargo
from high_risks import get_high_risks

raw = read_data(INPUT_PATH)
print("\nRaw file from source")
print(tabulate(raw, headers="keys", tablefmt="grid"))

cleaned = clean_data (raw)
#print ("Standardized data")
#print (tabulate (cleaned, headers="keys", tablefmt="grid"))

converted = convert_data (cleaned)
print ("\nconverted data")
print (tabulate(converted, headers="keys", tablefmt="grid"))

invalids, raw_valids = get_invalids_valids(converted)
print ("\ninvalids table")
print (tabulate (invalids, headers="keys", tablefmt="grid"))
print ("\nraw_valids table")
print (tabulate (raw_valids, headers="keys", tablefmt="grid"))

valids = get_valids(raw_valids)
print ("valid table")
print(tabulate(valids, headers="keys", tablefmt="grid"))

terminal_summary = summarize_terminal_cargo (valids)
print ("\nterminal cargo summary")
print(tabulate (terminal_summary, headers="keys", tablefmt="grid"))

high_risks = get_high_risks(valids)
print("\nhigh risks table")
print(tabulate(high_risks, headers="keys", tablefmt="grid"))