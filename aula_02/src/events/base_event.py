# --- Classes Base para Eventos ---

class BaseEvent:
    """
    Classe base para eventos. 
    Demonstra o conceito de encapsulamento: todos os eventos terão uma estrutura comum.
    """
    def __init__(self, name=""):
        self.name = name
        self.subscribers = []  # Lista de callbacks inscritos no evento
    
    def subscribe(self, callback):
        """Adiciona um callback à lista de inscritos."""
        self.subscribers.append(callback)
    
    def notify(self, data):
        """Notifica todos os inscritos com os dados passados."""
        for callback in self.subscribers:
            callback(data)

    def response(self):
        pass