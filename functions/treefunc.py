import csv

import math

import random

import pickle

import json

from collections import defaultdict

from PIL import Image, ImageDraw, ImageFont

import svgwrite

def calcEntropy(biežumi:list):
    # Nopietni?    ^

    E=0
    all_together=sum(biežumi)
    
    for b in biežumi:
        #print(f"-{b}/{all_together}log{b}/{all_together}", end=" ")
        if b!=0:
            E+= -1*((b/all_together)*math.log((b/all_together), 2))

    return E



def informationGain(entries_list):

    gains={}

    full_sum=len(entries_list)
    print(entries_list)

    print(f"\nHi. I am information gain function")
    print(f"\nThere are {full_sum} entries")


    for a in entries_list.getAttrib():

        print(f"I am looking at attribute {a}")

        BTable=entries_list.createBTable(a)

        for b in BTable:
            print(b, list(BTable[b].values()))

        information_gain=calcEntropy(list(BTable["xj"].values()))

        print(f"Entropija visam ir {information_gain}")

        for key, val in BTable.items():

            if key!="xj":
                row=list(val.values())
                information_gain-=(sum(row)/full_sum)*calcEntropy(row)

        gains[a]=information_gain

    return max(gains, key=gains.get)


class Entry:
    def __init__(self, klase, id, attributes:dict, row):
        self.attributes_dict=attributes
        self.row=row

        self.klase=klase
        self.id=id


    def __getitem__(self, key):
        return self.attributes_dict[key]
    
    def __str__(self):
        return f"Entry {self.id} with class {self.klase}"

    def __repr__(self):
        return self.__str__()
    

class Entry_list:
    def __init__(self):
        self.entries=[]

    def createBTable(self, attribute):
       
        print(f"\nHi. I am making BTable")
        print(f"I am not crazy I have {len(self.entries)} entries")

        klases=self.getKlases()
        
        BTable={"xj":{i:0 for i in klases}}

        for e in self.entries:
            if not e[attribute] in BTable:
                BTable[e[attribute]]=({i:0 for i in klases})
            
            BTable[e[attribute]][e.klase]+=1
            BTable["xj"][e.klase]+=1
        
        return BTable

    def getKlases(self):
        klases=[]
    
        for e in self.entries:
            if not e.klase in klases:
                klases.append(e.klase)

        return klases

    def getAttrib(self):
        return list(self.entries[0].attributes_dict.keys())

    def isUniform(self):
        is_uniform=True
        test_klase=self.entries[0].klase

        for e in self.entries:
            if e.klase!=test_klase:
                is_uniform=False
                break
        
        return is_uniform



    def find_unique(self, attribute):

        unique=[]
        for e in self.entries:
            val=e[attribute]
            if not val in unique:
                unique.append(val)
        
        return unique

    def split(self, attribute):


        split_dict={i:Entry_list() for i in self.find_unique(attribute)}

        for e in self.entries:

            val=e[attribute]

            split_dict[str(val)].append(e)
        
        return split_dict


    def append(self, entry:Entry):
        self.entries.append(entry)

    def __str__(self):
        return f"{self.entries}"

    def __repr__(self):
        return self.__str__()
    
    def __getitem__(self, index):
        return self.entries[index]

    def __len__(self):
        return len(self.entries)

class Node:
    def __init__(self, name, training_entries, splitting_attrib=None):
      self.name = name
      self.training_entries=training_entries
      self.splitting_attrib=splitting_attrib
      self.is_leaf=self.training_entries.isUniform()
      self.klase=self.training_entries.getKlases()[0]
    
    def __str__(self) -> str:
        return f"node.{self.name} split by {self.splitting_attrib} has {len(self.training_entries)} and is {self.is_leaf}"
    
    def __repr__(self) -> str:
        return self.__str__()

class Tree:
    def __init__(self, entries=None):
        self.structure = {}
        self.nodes = {}
        self.is_trained=False

        # Make training_entries optional
        if entries is not None:
            self.training_entries = entries
        else:
            self.training_entries = None  # or some default behavior if needed

    # Save the Tree object as a pickle file
    def save_as_pickle(self, file_path):
        with open(file_path, 'wb') as f:
            pickle.dump(self, f)

    # Load a Tree object from a pickle file
    @classmethod
    def load_from_pickle(cls, file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)

    # Save the Tree object as a JSON file (basic version)
    def save_as_json(self, file_path):
        # Convert only basic types to JSON
        with open(file_path, 'w') as f:
            json.dump(self.to_dict(), f)

    # Load a Tree object from a JSON file
    @classmethod
    def load_from_json(cls, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
            obj = cls()  # Create a Tree instance
            obj.from_dict(data)
            return obj

    # Helper to convert the object to a serializable dictionary for JSON
    def to_dict(self):
        return {
            "structure": self.structure,
            "nodes": self.nodes,
            # You can add more properties here as needed, ensuring they're serializable
        }

    # Helper to restore object from a dictionary (for JSON loading)
    def from_dict(self, data):
        self.structure = data.get("structure", {})
        self.nodes = data.get("nodes", {})
        # Handle other properties if needed

    def getNode(self, id):
        if id in self.nodes:
           return (True, self.nodes[id], id)
        return (False, "", "")
    
    def deleteNode(self, id):
        found= self.getNode(id)[0]

        if not found:
           return False
        
        del self.nodes[id]
        level=self.getNodeSubLevel(id[:-1])

        del level[id]

    
    def getNodeSubLevel(self, id):
        current = self.structure

        cur_key=""

        for p in id:
            cur_key+=p
            current = current[cur_key]

        return current


    def addSubNodeTo(self, node:Node, id, root=False):

        node_id=""

        if root:
            node_id=str(len(self.structure))
            self.structure[node_id]={}
            self.nodes[node_id] = node

        else:
            found, parent_node, parent_id = self.getNode(id)

            if not found:
                return False
            
            level=self.getNodeSubLevel(parent_id)

            node_id=parent_id+str(len(level))

            

            level[node_id]={}

            self.nodes[node_id]=node

        return node_id

    def mermaid(self):
        mermaid_string="graph TD"

        stack=[self.structure]

        while len(stack)>0:
            cur_stack_item=stack[0]

            for parent, children in cur_stack_item.items():
                for c, c_children in children.items():
                    mermaid_string+=f"\n    {parent}[{self.nodes[parent]}] --> {c}[{self.nodes[c]}]"

                    if c_children!={}:
                        stack.append({c:c_children})

            stack.pop(0)

        return mermaid_string
    

    # Example pug function that organizes data into lists
    def pug(self):
        keys = list(self.nodes.keys())
        
        # Calculate height (number of unique key lengths)
        height = len(set(len(key) for key in keys))
        
        # Group keys by length
        grouped_keys = defaultdict(list)
        for key in keys:
            grouped_keys[len(key)].append(key)
        
        # Create the final list of sublists, sorted based on the beginning of the string
        levels = [sorted(grouped_keys[length]) for length in sorted(grouped_keys.keys())]
        
        # Calculate width (maximum number of keys in any level)
        width = max(len(level) for level in levels)
        
        # Coordinates for all the nodes
        coords = {}
        
        # Calculate node coordinates (x, y positions)
        img_width = max(800, width * 200)  # Minimum width of 800 pixels
        img_height = height * 200  # Increased height for better visibility
        for row, level in enumerate(levels):
            y = (img_height / height) * row + (img_height / height / 2)
            if len(level) == 1:
                x_positions = [img_width / 2]
            else:
                spacing = img_width / (len(level) + 1)
                x_positions = [spacing * (i + 1) for i in range(len(level))]
            for col, node_key in enumerate(level):
                x = x_positions[col]
                coords[node_key] = (int(x), int(y))

        # Create lists of things to be drawn: lines, nodes, text
        lines = []  # Holds all the lines between nodes
        stack = [self.structure]
        while stack:
            cur_stack_item = stack.pop(0)
            for parent, children in cur_stack_item.items():
                for c, c_children in children.items():
                    lines.append((coords[parent], coords[c]))  # Line between parent and child
                    if c_children:
                        stack.append({c: c_children})

        nodes = []  # Holds node info (position, text, color)
        for n, c in coords.items():
            node = self.nodes[n]
            if node.is_leaf:
                text = node.klase
                elipse_col = (240, 255, 240)
                text_col = "black"
            else:
                elipse_col = (105, 105, 105)
                text_col = "white"
                text = node.splitting_attrib or node.name
            nodes.append((c, text, elipse_col, text_col))  # (position, text, ellipse color, text color)
        
        return lines, nodes, img_width, img_height

    # A: visualize function for PIL (returns a PIL image)
    def visualize(self):
        lines, nodes, w, h = self.pug()

        # Set up image dimensions
        img_width = w
        img_height = h
        img = Image.new('RGB', (img_width, img_height), color=(105, 105, 105))
        draw = ImageDraw.Draw(img)
        
        # Draw the lines first (edges between nodes)
        for line in lines:
            draw.line(line, fill="white", width=5)
        
        # Draw the nodes (ellipses) and the text
        radius = 40
        font_size = 25
        font = ImageFont.truetype(r"files\fonts\Roboto\Roboto-Medium.ttf", font_size)
        
        for node in nodes:
            (x, y), text, ellipse_color, text_color = node
            draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=ellipse_color)
            draw.text((x, y), text, fill=text_color, anchor="mm", font=font)
        
        return img

    # B: visualizeSVG function for svgwrite (returns an svgwrite object)
    def visualizeSVG(self):
        lines, nodes, w, h = self.pug()

        # Set up SVG drawing dimensions
        dwg = svgwrite.Drawing(size=(w, h))
        
        # Draw the lines first (edges between nodes)
        for line in lines:
            dwg.add(dwg.line(start=line[0], end=line[1], stroke=svgwrite.rgb(255, 255, 255), stroke_width=5))
        
        # Draw the nodes (circles) and the text
        radius = 40
        font_size = 25
        
        for node in nodes:
            (x, y), text, ellipse_color, text_color = node
            dwg.add(dwg.circle(center=(x, y), r=radius, fill=svgwrite.rgb(*ellipse_color)))
            dwg.add(dwg.text(text, insert=(x, y), text_anchor="middle", alignment_baseline="middle", font_size=font_size, fill=svgwrite.rgb(0, 0, 0) if text_color == 'black' else 'white'))
        
        return dwg



    def train(self):
        
        root_id=self.addSubNodeTo(Node("root", self.training_entries), '',  True)
        
        stack=[{root_id:self.nodes[root_id]}]

        while len(stack)>0:
            cur_stack_item=stack[0]
            
            for key, node in cur_stack_item.items():

                print(f"I am looking at {node}")

                entries=node.training_entries
                if not entries.isUniform():
                    split_by=informationGain(entries)

                    print(f"I decided to split by {split_by}")

                    splited=entries.split(split_by)
                    
                    for newname, newentries in splited.items():
                        sub_node_id=self.addSubNodeTo(Node(newname, newentries, split_by), key)

                        stack.append({sub_node_id:self.nodes[sub_node_id]})

                        print(f"    I got {newname} with {len(newentries)}")
                    

            stack.pop(0)

        self.is_trained=True


def read_csv_to_entries(path):
    entries = Entry_list()

    with open(path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            id_key, id=list(row.items())[0]
            klase_key, klase=list(row.items())[-1]

            other_columns_dict = {key: value for key, value in row.items() if key != id_key and key !=klase_key}
            full_row = row
            
            entry = Entry(klase, id, other_columns_dict, full_row)
            entries.append(entry)
    return entries

