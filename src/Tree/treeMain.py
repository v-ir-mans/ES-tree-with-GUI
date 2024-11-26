
import Tree.functions.fileReading as filer
import pickle, json

class Node:
    def __init__(self, name, training_entries, splitting_question=None):
      self.name = name
      self.training_entries=training_entries

      self.splitting_question=splitting_question

      self.is_leaf=self.training_entries.isUniform()

      self.klase=self.training_entries.getKlases()[0]

      self.id=Node

      self.cleardiv=True
    
    def __str__(self) -> str:
        return f"node.{self.name}"
    
    def __repr__(self) -> str:
        return self.__str__()

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

        node.id=node_id
        return node_id

    def getAllLeaves(self):
        leaves=[]

        for key, n in self.nodes.items():
            if n.is_leaf:
                leaves.append(key)
        
        return leaves

    def backtrackParents(self, key):
        parents=[]
        for i in range(len(key)-1):
            parents.append(key[:i+1])
        
        return parents
    
    def lawFromKey(self, key):
        parents=self.backtrackParents(key)

        law="JA "

        for n, p in enumerate(parents):
            
            curn=self.nodes[parents[n]]
            
            law+=f"'{curn.splitting_question}' "

            if n<len(parents)-1:

                law+=f"ir '{self.nodes[parents[n+1]].name}' UN "

        law+=f"ir '{self.nodes[key].name}' TAD ieraksts pieder klase '{self.nodes[key].klase}'"
            

        return(law)

    def getLaws(self):
        leaves=self.getAllLeaves()

        laws=""
        for l in leaves:
            laws+=self.lawFromKey(l)+"\n"

        return laws



    def saveLogic(self, text):
        self.logic_text+=f"\n{text}"

    def trainBinary(self):
        
        root_id=self.addSubNodeTo(Node("root", self.training_entries), '',  True)

        stack=[{root_id:self.nodes[root_id]}]


        while len(stack)>0:
            cur_stack_item=stack[0]
            
            for key, node in cur_stack_item.items():

                entries=node.training_entries

                if not node.is_leaf:

                    possible_splits={}

                    attribs=entries.getAttrib()

                    for a in attribs:
                        possible_splits[a]=entries.calculateQuestionValsForAttrib(a)


                    max_value = float('-inf')
                    attribute_to_split = None
                    question_to_split = None

                    for attrib, conditions in possible_splits.items():
                        for value, func in conditions:
                            if value > max_value:
                                max_value = value
                                attribute_to_split = attrib
                                question_to_split = func

                    if question_to_split==None:
                        #Nav iespējams sadalīt

                        node.is_leaf=True
                        node.cleardiv=False


                    else:


                        splited=entries.splitByQuestion(attribute_to_split, question_to_split)

                        node.splitting_question=question_to_split

                        
                        for newname, newentries in splited.items():


                            sub_node_id=self.addSubNodeTo(Node(newname, newentries, ''), key)

                            stack.append({sub_node_id:self.nodes[sub_node_id]})

                    
            stack.pop(0)

        #Deal with uncertain ones
        uncertain={}
        klases=self.training_entries.getKlases()



        for n in self.nodes:
            _, node, _ = self.getNode(n)
            if not(node.cleardiv):
                flip_last_bit = '1' if n[-1] == '0' else '0'
                sibling=self.getNode(n[:-1] + flip_last_bit)

                node.klase=[i for i in klases if i !=  sibling[1].klase][0]

        self.is_trained=True

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
                            child_text=child_node.splitting_question
                        
                        mermaid_string+=f"\n    {parent}[{parent_node.splitting_question}] -->|{child_node.name}| {c}[{child_text}]"

                        if c_children!={}:
                            stack.append({c:c_children})

                stack.pop(0)

            return mermaid_string
