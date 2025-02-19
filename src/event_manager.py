from src.event import Event

# --- Gerenciador de Eventos ---
class EventManager:
    """
    Gerencia o registro e a notificação dos eventos.
    Utiliza encapsulamento para ocultar a lógica interna de manipulação dos eventos.
    """
    __events = {}  # Dicionário para armazenar eventos registrados

    def register_event(event_name):
        """Registra um evento com um nome identificador."""
        EventManager.__events[event_name] = Event(event_name)

    def subscribe(event_name, callback):
        """Inscreve um callback em um evento registrado."""
        if event_name in EventManager.__events:
            EventManager.__events[event_name].subscribe(callback)
        else:
            print(f"[EventManager] Evento '{event_name}' não encontrado.")

    def notify(event_name, data):
        """Dispara um evento notificando todos os inscritos."""
        if event_name in EventManager.__events:
            EventManager.__events[event_name].notify(data)
        else:
            print(f"[EventManager] Evento '{event_name}' não encontrado.")
