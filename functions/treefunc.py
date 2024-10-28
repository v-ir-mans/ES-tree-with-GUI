import csv

import math

import random

import pickle

import json

from collections import defaultdict

from PIL import Image, ImageDraw, ImageFont

import svgwrite

import os, sys

import pandas as pd


def resource_path(relative_path):
    """ Get absolute path to resource, works for both source code and PyInstaller """
    # Check if the script is being executed in a bundle (PyInstaller)
    if hasattr(sys, '_MEIPASS'):
        # Running in PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # Running in source mode
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def calcEntropy(biežumi:list):
    # Nopietni?    ^

    E=0
    all_together=sum(biežumi)
    
    for b in biežumi:
        #print(f"-{b}/{all_together}log{b}/{all_together}", end=" ")
        if b!=0:
            E+= -1*((b/all_together)*math.log((b/all_together), 2))

    return E



def informationGain(entries_list, saveLogic):

    gains={}

    full_sum=len(entries_list)
    
    #print(entries_list)

    for a in entries_list.getAttrib():

        saveLogic(f"\n    Aplūkoju atribūtu '{a}'")
        saveLogic(f"        Izveidoju biežumu tabulu:")

        BTable=entries_list.createBTable(a)

        for b in BTable:
            saveLogic(f"\t\t{b}:\t{list(BTable[b].values())}")

        information_gain=calcEntropy(list(BTable["xj"].values()))

        #print(f"Entropija visam ir {information_gain}")

        for key, val in BTable.items():

            if key!="xj":
                row=list(val.values())
                information_gain-=(sum(row)/full_sum)*calcEntropy(row)

        saveLogic(f"\tInformation Gain sanāca: {information_gain}")
        if information_gain==0:
            saveLogic(f"\tKas ir loģiski. Šo varētu optimizēt un neizskatīt atribūtus ar entropiju 0. Armand!")

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
       
        #print(f"\nHi. I am making BTable")
        #print(f"I am not crazy I have {len(self.entries)} entries")

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
        return f"node.{self.name}"
    
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

        self.logic_text=""

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

                    parent_node=self.nodes[parent]
                    child_node=self.nodes[c]

                    if child_node.is_leaf:
                        child_text=child_node.klase
                    else:
                        child_text=child_node.splitting_attrib
                    
                    mermaid_string+=f"\n    {parent}[{parent_node.splitting_attrib}] -->|{child_node.name}| {c}[{child_text}]"

                    if c_children!={}:
                        stack.append({c:c_children})

            stack.pop(0)

        return mermaid_string
    

    def listsForVisualization(self):
        keys = list(self.nodes.keys())
        
        # Calculate height (number of unique key lengths) and group keys by length
        grouped_keys = defaultdict(list)
        for key in keys:
            grouped_keys[len(key)].append(key)
        
        # Create the final list of sublists, sorted based on the beginning of the string
        levels = [sorted(grouped_keys[length]) for length in sorted(grouped_keys.keys())]
        height = len(levels)
        
        # Calculate width (maximum number of keys in any level)
        width = max(len(level) for level in levels)
        
        # Coordinates for all the nodes
        coords = {}
        img_width = max(1600, width * 400)  # Minimum width of 800 pixels
        img_height = height * 400  # Adjust height for better visibility
        
        for row, level in enumerate(levels):
            y = (img_height / height) * row + (img_height / height / 2)
            if len(level) == 1:
                x_positions = [img_width / 2]
            else:
                spacing = img_width / (len(level) + 1)
                x_positions = [spacing * (i + 1) for i in range(len(level))]
            for col, node_key in enumerate(level):
                coords[node_key] = (int(x_positions[col]), int(y))

        # Lists to be returned: lines, nodes, mid_points, and child_names
        lines, mid_points, child_names = [], [], []
        
        # Traverse the tree and calculate line positions, mid-points, and child names
        stack = [self.structure]
        while stack:
            cur_stack_item = stack.pop(0)
            for parent, children in cur_stack_item.items():
                parent_coords = coords[parent]
                for child, child_children in children.items():
                    child_coords = coords[child]
                    lines.append((parent_coords, child_coords))  # Line between parent and child
                    
                    # Calculate the middle point of the line
                    mid_point = ((parent_coords[0] + child_coords[0]) // 2, 
                                (parent_coords[1] + child_coords[1]) // 2)
                    mid_points.append(mid_point)
                    
                    # Add child node's name
                    child_names.append(self.nodes[child].name)
                    
                    # Continue traversing if the child has children
                    if child_children:
                        stack.append({child: child_children})

        # Prepare node data (position, text, color)
        nodes = []
        for n, c in coords.items():
            node = self.nodes[n]
            if node.is_leaf:
                text = node.klase
            else:
                text = node.splitting_attrib or node.name
            nodes.append((c, text, node.is_leaf))
        
        return lines, nodes, img_width, img_height, mid_points, child_names


    # A: visualize function for PIL (returns a PIL image)
    def visualize(self):

        colors={"back":"#006769", "light":"#E6FF94", "middle":"#40A578", "prim":"#9DDE8B", "white":"#ffffff"}

        lines, nodes, w, h, mid_points, child_names = self.listsForVisualization()

        print(nodes)

        print(child_names)


        img = Image.new('RGB', (w, h), color=colors["back"])
        draw = ImageDraw.Draw(img)
        
        # Draw the lines first (edges between nodes)
        for line in lines:
            draw.line(line, fill=colors["middle"], width=7)
        
        # Draw the nodes (ellipses) and the text
        radius = 100
        font_size = 45
        
        font = ImageFont.truetype(resource_path(r"files/fonts/Roboto/Roboto-Bold.ttf"), font_size)
        
        for node in nodes:
            (x, y), text, is_leaf = node
            
            coords=(x - radius, y - radius, x + radius, y + radius)

            if is_leaf:
                draw.ellipse(coords, fill=colors["prim"])

                text_size = draw.textsize(text, font=font)
            
                # Define the rectangle coordinates (x, y) are the center coordinates
                rect_x0 = x - text_size[0] // 2 - 10  # 5 is padding
                rect_y0 = y - text_size[1] // 2 - 5  # 5 is padding
                rect_x1 = x + text_size[0] // 2 + 10
                rect_y1 = y + text_size[1] // 2 + 5
                
                # Draw the blue rectangle
                draw.rectangle([rect_x0, rect_y0, rect_x1, rect_y1], fill=colors["prim"])

                draw.text((x, y), text, fill=colors["back"], anchor="mm", font=font)
            else:
                draw.ellipse(coords, fill=colors["back"])
                draw.text((x, y), text, fill=colors["white"], anchor="mm", font=font)

        for n, point in enumerate(mid_points):
            (x, y) = point
            
            # Get the size of the text to determine the rectangle dimensions
            text_size = draw.textsize(child_names[n], font=font)
            
            # Define the rectangle coordinates (x, y) are the center coordinates
            rect_x0 = x - text_size[0] // 2 - 5  # 5 is padding
            rect_y0 = y - text_size[1] // 2 - 5  # 5 is padding
            rect_x1 = x + text_size[0] // 2 + 5
            rect_y1 = y + text_size[1] // 2 + 5
            
            # Draw the blue rectangle
            draw.rectangle([rect_x0, rect_y0, rect_x1, rect_y1], fill=colors["back"])
            
            # Draw the text on top of the rectangle
            draw.text((x, y), child_names[n], fill=colors["light"], anchor="mm", font=font)
        
        return img

    # B: visualizeSVG function for svgwrite (returns an svgwrite object)
    def visualizeSVG(self):
        # Get visualization data including mid_points and child_names
        lines, nodes, w, h, mid_points, child_names = self.listsForVisualization()
        
        # Define inverted B&W color scheme
        colors = {
            "back": "#FFFFFF",    # White background (inverted)
            "light": "#000000",   # Black text (inverted)
            "middle": "#808080",  # Gray for lines (unchanged)
            "prim": "#000000",    # Black for leaf nodes (inverted)
            "white": "#000000"    # Black (inverted)
        }
        
        # Scale down parameters
        scale = 0.7  # 70% of original size
        w = int(w * scale)
        h = int(h * scale)
        radius = int(70 * scale)  # Scaled down from 100
        font_size = int(32 * scale)  # Scaled down from 45
        
        # Set up SVG drawing
        dwg = svgwrite.Drawing(size=(w, h))
        
        # Create background rectangle
        dwg.add(dwg.rect(insert=(0, 0), size=(w, h), fill=colors["back"]))
        
        # Draw the lines first (edges between nodes)
        for line in lines:
            # Scale the line coordinates
            start = (int(line[0][0] * scale), int(line[0][1] * scale))
            end = (int(line[1][0] * scale), int(line[1][1] * scale))
            dwg.add(dwg.line(
                start=start,
                end=end,
                stroke=colors["middle"],
                stroke_width=int(7 * scale)
            ))
        
        # Draw the nodes (circles) and text
        for node in nodes:
            (x, y), text, is_leaf = node
            # Scale coordinates
            x = int(x * scale)
            y = int(y * scale)
            
            if is_leaf:
                # Leaf nodes
                # Add circle
                dwg.add(dwg.circle(
                    center=(x, y),
                    r=radius,
                    fill=colors["prim"]
                ))
                
                # Calculate text size (approximate for SVG)
                text_width = len(text) * (font_size * 0.6)
                text_height = font_size * 1.2
                
                # Add rectangle behind text
                rect_x0 = x - text_width/2 - 10 * scale
                rect_y0 = y - text_height/2 - 5 * scale
                rect_width = text_width + 20 * scale
                rect_height = text_height + 10 * scale
                
                dwg.add(dwg.rect(
                    insert=(rect_x0, rect_y0),
                    size=(rect_width, rect_height),
                    fill=colors["prim"]
                ))
                
                # Add text
                dwg.add(dwg.text(
                    text,
                    insert=(x, y),
                    font_size=font_size,
                    font_family="Roboto-Bold",
                    text_anchor="middle",
                    dominant_baseline="middle",
                    fill=colors["back"]  # White text on black background
                ))
            else:
                # Non-leaf nodes
                dwg.add(dwg.circle(
                    center=(x, y),
                    r=radius,
                    fill=colors["back"],
                    stroke=colors["light"],
                    stroke_width=int(2 * scale)
                ))
                
                dwg.add(dwg.text(
                    text,
                    insert=(x, y),
                    font_size=font_size,
                    font_family="Roboto-Bold",
                    text_anchor="middle",
                    dominant_baseline="middle",
                    fill=colors["light"]
                ))
        
        # Add child names at midpoints
        for n, point in enumerate(mid_points):
            (x, y) = point
            # Scale coordinates
            x = int(x * scale)
            y = int(y * scale)
            text = child_names[n]
            
            # Calculate text size (approximate for SVG)
            text_width = len(text) * (font_size * 0.6)
            text_height = font_size * 1.2
            
            # Add rectangle behind text
            rect_x0 = x - text_width/2 - 5 * scale
            rect_y0 = y - text_height/2 - 5 * scale
            rect_width = text_width + 10 * scale
            rect_height = text_height + 10 * scale
            
            dwg.add(dwg.rect(
                insert=(rect_x0, rect_y0),
                size=(rect_width, rect_height),
                fill=colors["back"],
                stroke=colors["light"],
                stroke_width=int(1 * scale)
            ))
            
            # Add text
            dwg.add(dwg.text(
                text,
                insert=(x, y),
                font_size=font_size,
                font_family="Roboto-Bold",
                text_anchor="middle",
                dominant_baseline="middle",
                fill=colors["light"]
            ))
        
        return dwg

    def saveLogic(self, text):
        self.logic_text+=f"\n{text}"

    def train(self):
        
        root_id=self.addSubNodeTo(Node("root", self.training_entries), '',  True)
        
        stack=[{root_id:self.nodes[root_id]}]

        self.saveLogic(f"Sākas, koka izveide")
        self.saveLogic(f"Izveidoju saknes mezglu ar id {root_id}")

        while len(stack)>0:
            cur_stack_item=stack[0]
            
            for key, node in cur_stack_item.items():

                self.saveLogic(f"Aplūko mezglu {node} ar id {key}")

                if node.is_leaf:
                    self.saveLogic(f"Tas ir lapas mezgls. Super! ☘️😃")
                else:
                    self.saveLogic(f"Tas nav lapas mezgls, līdz ar to, to nāksies sašķelt.")

                entries=node.training_entries

                if not node.is_leaf:

                    self.saveLogic(f"Šajā mezglā ir {len(entries)} vienumi")
                    self.saveLogic(f"Aprēķinu Information gain visiem atribūtiem")

                    split_by=informationGain(entries, self.saveLogic)

                    self.saveLogic(f"Mezglu vajag sasķelt izmantojot atribūtu '{split_by}'.")

                    node.splitting_attrib=split_by

                    splited=entries.split(split_by)
                    
                    self.saveLogic(f"Izveidojās {len(splited)} jauni mezgli:")

                    for newname, newentries in splited.items():


                        sub_node_id=self.addSubNodeTo(Node(newname, newentries, ''), key)

                        self.saveLogic(f"   {self.nodes[sub_node_id]} (id={sub_node_id})")

                        stack.append({sub_node_id:self.nodes[sub_node_id]})

                        #print(f"    I got {newname} with {len(newentries)}")
                    
            self.saveLogic("\n")
            stack.pop(0)

        self.is_trained=True
        self.saveLogic("Koks ir izaudzis! 🌳")


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


# ChatGPT 100%
def read_excel_to_entries(path, sheet_name=0):
    entries = Entry_list()
    
    # Read the Excel file into a DataFrame
    df = pd.read_excel(path, sheet_name=sheet_name, dtype=str)
    
    # Iterate over each row in the DataFrame
    for _, row in df.iterrows():
        # Extract the first and last columns as id and klase, and convert them to strings
        id_key, id = str(row.index[0]), str(row.iloc[0])
        klase_key, klase = str(row.index[-1]), str(row.iloc[-1])
        
        # Create a dictionary of other columns except id and klase, ensuring all values are strings
        other_columns_dict = {str(key): str(row[key]) for key in row.index if key != id_key and key != klase_key}
        
        # Convert the entire row to a dictionary with all values as strings
        full_row = {str(key): str(value) for key, value in row.to_dict().items()}
        
        # Create and append an Entry object
        entry = Entry(klase, id, other_columns_dict, full_row)
        entries.append(entry)
    
    return entries