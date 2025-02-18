from .base_event import BaseEvent

# Evento específico para mensagens, utilizando herança da BaseEvent
class MessageEvent(BaseEvent):
    def __init__(self):
        super().__init__(name="MessageEvent")

    def faz_alguma_coisa(self):
        print("Fazendo alguma coisa...")

    def response(self):
        pass