from flask import Flask
from src.app_controler import AppController
from src.event_manager import EventManager
from src.events.message_event import MessageEvent 
from src.events.error_event import ErrorEvent
from src.observers.logger import Logger
from src.observers.analytics import Analytics

def create_app():
    # --- Configuração do Flask e Eventos ---
    app = Flask(__name__)
    event_manager = EventManager()

    # Instanciando os eventos específicos
    message_event = MessageEvent()
    error_event = ErrorEvent()

    # Registrando os eventos no gerenciador
    event_manager.register_event("MessageEvent", message_event)
    event_manager.register_event("ErrorEvent", error_event)

    # Criando instâncias dos observadores
    logger = Logger()
    analytics = Analytics()

    # Inscrevendo os observadores aos eventos usando o padrão Observer
    event_manager.subscribe("MessageEvent", logger.log)
    event_manager.subscribe("MessageEvent", analytics.process)
    event_manager.subscribe("ErrorEvent", logger.log)

    # Instanciando o controlador da aplicação, separando a configuração de rotas do restante da lógica
    controller = AppController(app, event_manager)
    return app

if __name__ == '__main__':
    # Inicia o servidor Flask em modo debug
    app = create_app()
    app.run(debug=True)
