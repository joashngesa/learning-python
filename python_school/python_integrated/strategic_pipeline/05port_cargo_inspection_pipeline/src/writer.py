
import os
import csv

def write_output(file_path,data,output_delimiter,column_names):

    output_folder = os.path.dirname (file_path)

    if output_folder:
        os.makedirs (output_folder,exist_ok=True)

    with open (file_path, "w", newline="") as file:
        writer = csv.DictWriter (file,delimiter=output_delimiter,fieldnames=column_names,extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)
        print("write to: ",os.path.abspath(file_path))