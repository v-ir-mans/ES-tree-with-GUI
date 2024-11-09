from Tree.treeMain import Tree
import Tree.functions.fileReading as filer
from Tree.Classes.EntryClasses import Question
entries=filer.read_csv_to_entries(r'.\test_data\data_test.csv')
attribs=entries.getAttrib()
print(attribs)


for a in attribs:
    entries.createAllAttributeBinaryBTables(a) 
    break