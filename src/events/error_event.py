from .base_event import BaseEvent

# Evento específico para erros, também utilizando herança da BaseEvent
class ErrorEvent(BaseEvent):
    def __init__(self):
        BaseEvent.__init__(self, name="ErrorEvent")
