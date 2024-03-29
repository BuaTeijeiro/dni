from src.tablaAsignacion import TablaAsignacion

class Dni:
    #Añadir la longitud de la cadena del dni como variable global, por si cambia.
    DNI_NUMBER_LENGTH = 8
    
    def __init__(self,number='00000000',letter=''):
        self.number = str(number)
        self.letter = str(letter)
        self.table = TablaAsignacion()
        self.validity = self.isDniValid()
    
    def getNumber(self):
        return self.number
    
    def getLetter(self):
        return self.letter
    
    def getDni(self):
        return self.getNumber() + self.getLetter()
    
    def getTable(self):
        return self.table
    
    def getValidity(self):
        return self.validity
    
    def isNumberValid(self):
        number = self.getNumber()
        return number.isdigit() and len(number) == Dni.DNI_NUMBER_LENGTH
    
    def computeValidLetter(self):
        table = self.getTable()
        return table.getDniLetter(self.getNumber())
        
    def isDniValid(self):
        return self.getLetter() == self.computeValidLetter() if self.isNumberValid() else False
        
    def __repr__(self):
        return self.getDni()
        

    
        
    
    
    