from abc import ABC, abstractmethod
from src.core.entities import Order, Payment

class IpaymentStrategy(ABC):
    """
    Contrato (interface) para qualquer método de pagamento.
    Define que toda estratégia deve saber processar um pagamento.
    """
    @abstractmethod
    def process_payment(self, order: Order) -> dict:
        pass

class IpaymentRepository(ABC):
    """
    Contrato (interface) para salvar os pagamentos no BD.
    """
    @abstractmethod
    def save(self, payment: Payment) -> None:
        pass