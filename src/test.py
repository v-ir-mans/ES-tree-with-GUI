from Tree.treeMain import Tree
import Tree.functions.fileReading as filer

entries=filer.read_csv_to_entries(r'.\test_data\data.csv')

print(entries)