# --- Observadores (Observers) ---

class Logger:
    """
    Observador que registra (log) os dados recebidos.
    Demonstra o padrão Observer: reage a notificações de eventos.
    """
    def log(self, data):
        print(f"[Logger] Dados recebidos: {data}")
