from strategies import IPaymentStrategy

class PaymentContext:
    """
    O Contexto. É a classe que o "cliente" (nossa API) vai usar.
    Ele não sabe qual é a lógica do pagamento, apenas
    guarda uma referência para a estratégia "plugada".
    """
    def __init__(self, strategy: IPaymentStrategy):
        self._strategy = strategy
        
    def execute_payment(self, amount: float) -> dict: # <--- CORRIGIDO AQUI (era execute_paymant)
        """
        O contexto DELEGA a execução do pagamento para a estratégia.
        """
        print("Contexto: Executando o pagamento...")
        # <--- CORRIGIDO AQUI (era self.strategy)
        return self._strategy.process_payment(amount)