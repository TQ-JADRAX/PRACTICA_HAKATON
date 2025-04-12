from abc import ABC, abstractmethod

class Cuenta_Bancaria(ABC):
    def __init__(self, titular, saldo_inicial):
        self._titular = titular
        self._saldo = saldo_inicial

   
    
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter    
    def saldo(self, saldo):
        self._saldo = saldo
    
    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, titular):
        self._titular = titular
 
    @abstractmethod
    def info(self):
        pass
    def Depositar(self):
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad a depositar: "))
                if cantidad > 0:
                    self._saldo += cantidad
                    break
                else:
                    print("La cantidad a depositar debe ser mayor que 0")
            except (ValueError, TypeError):
                print("La cantidad a depositar debe ser un número")
    def Retirar(self):    
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad a retirar: "))
                if cantidad > 0:
                    self._saldo -= cantidad
                    break
                else:
                    print("La cantidad a retirar debe ser mayor que 0") 
            except (ValueError, TypeError):
                print("La cantidad a retirar debe ser un número")
    ''' def  TRANSFERIR(self):
        while true:
            try:
    '''
    #def INFO(self):

    
        
        


