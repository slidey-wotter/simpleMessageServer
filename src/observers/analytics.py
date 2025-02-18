# --- Observadores (Observers) ---

class Analytics:
    """
    Observador que processa os dados para análise.
    Outro exemplo do padrão Observer.
    """
    def process(self, data):
        if 'analise' in data:
            print(f"[Analytics] Não quero mais aula")
        print(f"[Analytics] Processando dados: {data}")
        