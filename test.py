from functions import treefunc as treef

csv_entries=treef.read_csv_to_entries(r"C:\Users\olive\Documents\2darbs\Backend\data\training\data_test.csv")
excel_entries=treef.read_excel_to_entries(r"C:\Users\olive\Documents\2darbs\Backend\data\training\dati_slim-ves.xlsx")

print(csv_entries)

print(excel_entries)