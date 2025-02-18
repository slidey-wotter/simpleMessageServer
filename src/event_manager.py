# --- Gerenciador de Eventos ---
class EventManager:
    """
    Gerencia o registro e a notificação dos eventos.
    Utiliza encapsulamento para ocultar a lógica interna de manipulação dos eventos.
    """
    def __init__(self):
        self.events = {}  # Dicionário para armazenar eventos registrados

    def register_event(self, event_name, event_obj):
        """Registra um evento com um nome identificador."""
        self.events[event_name] = event_obj

    def subscribe(self, event_name, callback):
        """Inscreve um callback em um evento registrado."""
        if event_name in self.events:
            self.events[event_name].subscribe(callback)
        else:
            print(f"[EventManager] Evento '{event_name}' não encontrado.")

    def notify(self, event_name, data):
        """Dispara um evento notificando todos os inscritos."""
        if event_name in self.events:
            self.events[event_name].notify(data)
        else:
            print(f"[EventManager] Evento '{event_name}' não encontrado.")
