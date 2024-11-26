import math

def calcEntropy(biežumi:list):
    # Nopietni?    ^

    E=0
    all_together=sum(biežumi)
    
    for b in biežumi:
        #print(f"-{b}/{all_together}log{b}/{all_together}", end=" ")
        if b!=0:
            E+= -1*((b/all_together)*math.log((b/all_together), 2))

    return E