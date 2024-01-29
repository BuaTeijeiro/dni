from src.dni import Dni

if __name__ == '__main__':
    dnis = ['53976108F', '39514159K','00000000A']
    
    for code in dnis:
        dni = Dni(code[:-1],code[-1])
        validity = 'Valid' if dni.isDniValid() else 'Invalid'
        print(f'Dni with number {dni} is:\t {validity}')
  