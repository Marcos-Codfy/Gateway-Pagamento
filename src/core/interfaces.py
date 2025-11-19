from abc import ABC, abstractmethod
from typing import Dict
from src.core.entities import Order, Payment

class IpaymentStrategy(ABC):
    """"
    Contrato (interface) para qualquer método de pagamento
    (Pix, Cartão, Boleto)
    """
    pass

class IpaymentRepository(ABC):
    """"
    Contrato (interface) para salvar os pagamentos no BD
    Isso permite que a gente use o "Banco Fake" nos teste e o SQL no real
    """
    @abstractmethod
    def save(self,payment: Payment) -> None:
        pass