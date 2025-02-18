from .base_event import BaseEvent

# Evento específico para mensagens, utilizando herança da BaseEvent
class MessageEvent(BaseEvent):
    def __init__(self):
        BaseEvent.__init__(self, name="MessageEvent")
