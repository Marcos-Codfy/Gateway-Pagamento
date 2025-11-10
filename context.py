from strategies import IPaymentStrategy

class PaymantCOntext:
    """
    O Contexto. É a classe que o "cliente" (nossa API) vai usar.
    Ele não sabe qual é a lógica do pagamento, apenas
    guarda uma referência para a estratégia "plugada".
    """
    def __init__(self, strategy: IPaymentStrategy):
        self._strategy = strategy
        
    def execute_paymant(self, amount: float) -> dict:
        """
        O contexto DELEGA a execução do pagamento para a estratégia.
        """
        print("Contexto: Executando o pagamento...")
        return self.strategy.process_payment(amount)