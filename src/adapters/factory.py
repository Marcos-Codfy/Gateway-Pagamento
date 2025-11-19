from src.core.interfaces import IpaymentStrategy
from src.adapters.strategies import PIxStrategy, CreditCardStrategy, BoletoStrategy

class PaymentStrategyFactory:
    """
    Factory Method: Responsável por criar a instância correta
    da estratégia baseada em uma string (ex: 'pix')
    """
    
    @staticmethod
    def get_strategy(method: str) -> IpaymentStrategy:
        if method == 'pix':
            return PIxStrategy()
        elif method == 'credit_card':
            return CreditCardStrategy()
        elif method == 'boleto':
            return BoletoStrategy()
        
        #Lança erro se o método não existir
        raise ValueError(f"Payment method '{method}' is not supported.")