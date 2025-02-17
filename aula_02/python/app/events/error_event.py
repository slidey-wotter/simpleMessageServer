from .base import BaseEvent

class ErrorEvent(BaseEvent):
    def __init__(self):
        super().__init__(name="ErrorEvent")
