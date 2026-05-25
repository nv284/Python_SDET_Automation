from openpyxl import load_workbook
from zipfile import BadZipFile

file_path = r"week-3\day-2\data_driven_api\users.xlsx"

try:

    workbook = load_workbook(file_path)

    print("Excel file loaded successfully")

except FileNotFoundError:
    
    print("File not found")

except BadZipFile:
    
    print("Invalid Excel file or corrupted file")

except PermissionError:
    
    print("Close the Excel file before running script")