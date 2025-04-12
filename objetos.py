from main import CUENTA_BANCARIA

cuenta0 = CUENTA_BANCARIA("Tapia",100)

cuenta1 = CUENTA_BANCARIA("Alfedro",170)

cuenta2 = CUENTA_BANCARIA("Bruno",200)
from main import *


class Cuenta_Inicial(Cuenta_Bancaria):
    def info(self):
        print(f'Titular: {self.titular}')
        print(f'Saldo disponible: {self.saldo}')


cuenta1 = Cuenta_Inicial('Luis',2000)
cuenta2 = Cuenta_Inicial('Alexys',2000)
cuenta3 = Cuenta_Inicial('Migue',2000)
cuenta1.info()
cuenta1.Depositar()
cuenta1.info()
cuenta1.Retirar()

