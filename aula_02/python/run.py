from flask import Flask
from app.event_manager import EventManager
from app.events.message_event import MessageEvent
from app.events.error_event import ErrorEvent
from app.observers.logger import Logger
from app.observers.analytics import Analytics
from app.controllers.app_controller import AppController

def create_app():
    app = Flask(__name__)
    event_manager = EventManager()

    # Instanciando os eventos
    message_event = MessageEvent()
    error_event = ErrorEvent()

    # Registrando os eventos no gerenciador
    event_manager.register_event("MessageEvent", message_event)
    event_manager.register_event("ErrorEvent", error_event)

    # Criando instâncias de observadores
    logger = Logger()
    analytics = Analytics()

    # Inscrevendo observadores aos eventos
    event_manager.subscribe("MessageEvent", logger.log)
    event_manager.subscribe("MessageEvent", analytics.process)
    event_manager.subscribe("ErrorEvent", logger.log)

    # Instanciando o controlador da aplicação
    AppController(app, event_manager)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
