

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
        
if __name__ == '__main__':
    tabla = TablaAsignacion()
    print(tabla)
    