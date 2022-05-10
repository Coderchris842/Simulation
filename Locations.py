import People
# Model of place
class place:
    name = "void"
    # What places are nearby = close
    close1 = "void"
    close2 = "void"
    close3 = "void"
    close4 = "void"
    pop = 0
    def checkpop(self):
        # checks pop in a place
        i = 0
        place.pop = 0
        temppop = list(People.pop)
        for m in People.pop:
            if People.pop[temppop[i]].abstract.location == place.name:
                place.pop+=1
            i+=1
    def __init__(self, name, close1, close2, close3, close4):
        self.name = name
        self.close1 = close1
        self.close2 = close2
        self.close3 = close3
        self.close4 = close4
                
Void = place("void", "void", "void", "void", "void")
Void.checkpop()
