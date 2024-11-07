from functions import treefunc as treef

csv_entries=treef.read_csv_to_entries(r"C:\Users\olive\Documents\2darbs\Backend\data\training\data_test.csv")

tree=treef.Tree(csv_entries)

print(tree.training_entries.getAttrib())

it=treef.calcEntropy([6, 9])
itl=treef.calcEntropy([2, 0])
itr=treef.calcEntropy([4, 9])

pL=2/15
pR=13/15

print(it-pL*itl-pR*itr)
