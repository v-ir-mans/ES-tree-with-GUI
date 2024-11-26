from Tree.treeMain import Tree
import Tree.functions.fileReading as filer
from Tree.Classes.EntryClasses import Question

import pyperclip



entries=filer.read_excel_to_entries(r'.\test_data\real.xlsx')



tree=Tree(entries=entries)

tree.trainBinary()
pyperclip.copy(tree.mermaid())
