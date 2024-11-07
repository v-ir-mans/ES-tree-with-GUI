
import Tree.functions.fileReading as filer

class Tree:
    def __init__(self, entries=None):

        self.structure = {}
        self.nodes = {}
        self.is_trained=False

        if entries is not None:
            self.training_entries = entries
        else:
            self.training_entries = None 

        self.logic_text=""


