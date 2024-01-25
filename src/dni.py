from src.tablaAsignacion import TablaAsignacion

class Dni:
    def __init__(self,number='00000000',letter=''):
        self.number = str(number)
        self.letter = str(letter)
        self.table = TablaAsignacion()
        self.valid = self.checkValidity()
    
    def getNumber(self):
        return self.number
    
    def getLetter(self):
        return self.letter
    
    def getTable(self):
        return self.table
    
    def getValidity(self):
        return self.valid
    
    def checkNumber(self):
        number = self.getNumber()
        return number.isdigit() and len(number) == 8
        
    def checkValidity(self):
        return self.letter == self.table.getDniLetter(self.getNumber()) if self.checkNumber() else False
        
    def __repr__(self):
        if self.valid:
            return self.getNumber() + self.getLetter()
        else:
            return 'Para que quieres ver esto si no es válido'
        
if __name__ == '__main__':
    print(Dni('53976108','F'))
    print(Dni('53976108','H'))
    print(Dni('39451213','A'))
    print(Dni('52938234',''))
    
        
    
    
    