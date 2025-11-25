from src.core.interfaces import IpaymentStrategy
from src.adapters.strategies import PixStrategy, CreditCardStrategy, BoletoStrategy

class PaymentStrategyFactory:
    """
    Factory Method: Responsible for creating the correct strategy instance
    based on a string (e.g., 'pix').
    """
    
    @staticmethod
    def get_strategy(method: str) -> IpaymentStrategy:
        if method == 'pix':
            return PixStrategy()
        elif method == 'credit_card':
            return CreditCardStrategy()
        elif method == 'boleto':
            return BoletoStrategy()
        
        # Raises error if method does not exist
        raise ValueError(f"Payment method '{method}' is not supported.")