import os
import csv

def write_output(output_path,data,output_delimiter,output_column):
    folder_path = os.path.dirname(output_path)

    if folder_path:
        os.makedirs(folder_path, exist_ok=True)

    with open (output_path, "w", newline="") as file:
        writer = csv.DictWriter (file,delimiter=output_delimiter,fieldnames=output_column,extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)
        print("write to: ",os.path.abspath(output_path))

