from itertools import combinations
import inspect

class Attribute:
    def __init__(self, attribute_name, value):
        self.attribute_name = attribute_name
        self.is_float = self._is_float(value)
        if self.is_float:
            self.value = float(value)
        else:
            self.value = value
        
    
    def _is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def __repr__(self):
        return f"Attribute(attribute_name={self.attribute_name}, value={self.value}, is_float={self.is_float})"

class Question:
    def __init__(self, lambda_str):
      self.lambda_str = lambda_str
      self.func=eval(self.lambda_str)
    def ask(self, value):
        return self.func(value)

    def __repr__(self):
        return self.lambda_str
    
class Entry:
    def __init__(self, klase, id, attributes:dict, row):
        self.attributes_dict={}

        for ak, av in attributes.items():
            self.attributes_dict[ak]=Attribute(ak, av)

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

    def findUnique(self, attribute):

        unique=[]
        for e in self.entries:
            val=e[attribute].value
            if not val in unique:
                unique.append(val)
        
        return unique


    def createBinaryBTable(self, attribute, question):

        klases=self.getKlases()
        
        PL=[]
        PR=[]

        for e in self.entries:
            value=e[attribute].value
            if question.ask(value)==True:
                PL.append(value)
            else:
                PR.append(value)

        print(f"\n{question} : {len(PL)}/{len(PR)}")
        
        return "BTable"

    def createAllAttributeBinaryBTables(self, attribute):
        questions=self.constructQuestions(attribute)

        for q in questions:
            self.createBinaryBTable(attribute, q)

    def constructQuestions(self, attribute):
        unique=self.findUnique(attribute)

        question_list=[]

        if type(unique[0])==float:
            unique.sort()

            for u in unique[:-1]:
                question=Question(f"lambda x: x<={u}")
                question_list.append(question)
        else:
            combinations_list=[]
            for i in range(1, len(unique)):
                comb=[list(sublist) for sublist in combinations(unique, i)]
                combinations_list.extend(comb)
            
            for c in combinations_list:
                question=Question(f"lambda x: x in {c}?")
                question_list.append(question)
        return question_list

    def split(self, attribute):


        split_dict={i:Entry_list() for i in self.find_unique(attribute)}

        for e in self.entries:

            val=e[attribute].value

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