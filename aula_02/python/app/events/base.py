class BaseEvent:
    def __init__(self, name=""):
        self.name = name
        self.subscribers = []
    
    def subscribe(self, callback):
        """Inscreve um callback para o evento."""
        self.subscribers.append(callback)
    
    def notify(self, data):
        """Notifica todos os inscritos com os dados fornecidos."""
        for callback in self.subscribers:
            callback(data)
