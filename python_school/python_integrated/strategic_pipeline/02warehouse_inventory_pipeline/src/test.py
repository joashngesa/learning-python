#i am really struggling with modules, in the next lesson, tackle this topicx with the understanding that 
#my knowledge and unserstanding is abysmall. 
from tabulate import tabulate
from reader import read_data
from config import INPUT_PATH
from converter import convert_data
from invalids_valid_sifter import sifter
from invalids_valid_sifter import duplicate_data
from transformer import transform_data
from summary import summarize_data

if __name__=="__main__":

    raw = read_data(INPUT_PATH)
    #print("raw data")
    #print(tabulate(raw, headers="keys", tablefmt="grid"))

    converted = convert_data(raw)
    #print("\nconverted data")
    #print(tabulate(converted, headers="keys", tablefmt="grid"))

    invalids, valids = sifter(converted)
    duplicates = duplicate_data(invalids)
    print("duplicate data")
    print(tabulate(duplicates, headers="keys", tablefmt="grid"))
    print("\n invalid table")
    print(tabulate(invalids, headers="keys", tablefmt="grid"))
    print("\nvalid table")
    print(tabulate(valids, headers="keys", tablefmt="grid"))

    transformed = transform_data(valids)
    print("\ntransformed table")
    print(tabulate(transformed, headers="keys", tablefmt="grid"))

    summary = summarize_data(transformed)
    print("\nsummary")
    print(tabulate(summary, headers="keys", tablefmt="grid"))