from .base import BaseEvent

class MessageEvent(BaseEvent):
    def __init__(self):
        super().__init__(name="MessageEvent")
