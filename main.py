from abc import ABC, abstractmethod

class CUENTA_BANCARIA(ABC):
    def __init__(self, titular, saldo_inicial):
        self._titular = titular
        self._saldo = saldo_inicial

    def depositar(self, cantidad):
        self._saldo += cantidad

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
    
    
    
        
        
        
        