from abc import ABC, abstractmethod

class CUENTA_BANCARIA(ABC):
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
    def info(self, cantidad):
        pass
    def DEPOSITAR(self):
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
    def RETIRAR(self):    
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
    
    
    
        
        
obj = CUENTA_BANCARIA("Juan Pérez", 2000)
obj2 = CUENTA_BANCARIA("Santiago Lopez", 2000)
obj3 = CUENTA_BANCARIA("Javier Rodriguez", 2000)

print(obj.info(0))
print(obj2.info(0))
print(obj3.info(0))


