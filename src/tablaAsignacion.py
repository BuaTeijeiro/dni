

class TablaAsignacion:
    def __init__(self):
        self.tabla = [
            "T",
            "R",
            "W",
            "A",
            "G",
            "M",
            "Y",
            "F",
            "P",
            "D",
            "X",
            "B",
            "N",
            "J",
            "Z",
            "S",
            "Q",
            "V",
            "H",
            "L",
            "C",
            "K",
            "E",
        ]
    
    def getTable(self):
        return self.tabla
        
    def __repr__(self):
        return " ".join(self.getTable())
    
    def getmodule(self):
        return len(self.getTable())
    
    def getLetter(self, position):
        try:
            return self.tabla[position]
        except:
            return 'No hay ninguna letra asociada a esta posición'
        
    def isLetterAllowed(self,letter):
        return letter in self.getTable()
    
    def getDniLetter(self,dni):
        dniLetterPosition = int(dni) % self.getmodule()
        return self.getLetter(dniLetterPosition)
        
if __name__ == '__main__':
    tabla = TablaAsignacion()
    print(tabla)
    