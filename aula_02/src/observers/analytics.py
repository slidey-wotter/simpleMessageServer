# --- Observadores (Observers) ---

class Analytics:
    """
    Observador que processa os dados para análise.
    Outro exemplo do padrão Observer.
    """
    def process(self, data):
        print(f"[Analytics] Processando dados: {data}")
        