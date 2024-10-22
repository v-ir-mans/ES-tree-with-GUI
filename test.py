from functions import treefunc as treef

tree=treef.Tree(treef.read_csv_to_entries(r"C:\Users\olive\Documents\2darbs\Backend\data\training\data.csv"))
tree.train()
img=tree.visualize()

img.show()

img=tree.visualize()

img=tree.visualizeSVG()

img.saveas('output.svg')