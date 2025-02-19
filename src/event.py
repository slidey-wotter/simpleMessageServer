# --- Classes Base para Eventos ---

class Event:
    """
    Classe base para eventos.
    Demonstra o conceito de encapsulamento: todos os eventos terão uma estrutura comum.
    """
    def __init__(self, name):
        self.name = name
        self.__subscribers = []  # Lista de callbacks inscritos no evento

    def subscribe(self, callback):
        """Adiciona um callback à lista de inscritos."""
        self.__subscribers.append(callback)

    def notify(self, data):
        """Notifica todos os inscritos com os dados passados."""
        for callback in self.__subscribers:
            callback(data)
