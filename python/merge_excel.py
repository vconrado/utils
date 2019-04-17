import os
import pandas as pd


base_path = "/source_files"
output_file = "merged.xlsx"

# discovering files

included_extensions = ['xls','xlsx']
file_names = [fn for fn in os.listdir(base_path)
              if any(fn.endswith(ext) for ext in included_extensions)]

print("Files: ", file_names)

writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

# reading files
for file_name in file_names:
    try:
        file_path = "{}/{}".format(base_path,file_name)
        xl = pd.ExcelFile(file_path)
        # for each sheet in xls file
        for sheet_name in xl.sheet_names:
            df = xl.parse(sheet_name)
            df.to_excel(writer, sheet_name)
    except Exception as ex:
        print("Could open file {}. Skipping it... ".format(file_path))

writer.save()

