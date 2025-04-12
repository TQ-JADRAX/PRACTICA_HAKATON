from main import Cuenta_Bancaria

cuenta0 = Cuenta_Bancaria("Tapia",100)

cuenta1 = Cuenta_Bancaria("Alfedro",170)

cuenta2 = Cuenta_Bancaria("Bruno",200)
from main import *


class Cuenta_Inicial(Cuenta_Bancaria):
    def info(self):
        print(f'Titular: {self.titular}')
        print(f'Saldo disponible: {self.saldo}')


cuenta1 = Cuenta_Inicial('Luis',2000)
cuenta2 = Cuenta_Inicial('Alexys',2000)
cuenta3 = Cuenta_Inicial('Migue',2000)
cuenta1.info()



