from flask import Flask
from src.app_controler import AppController
from src.event_manager import EventManager
from src.events.message_event import MessageEvent
from src.events.error_event import ErrorEvent
from src.observers.logger import Logger
from src.observers.analytics import Analytics

class App(Flask):
    def __init__(self):
      # --- Configuração do Flask e Eventos ---
      Flask.__init__(self, __name__)

      event_manager = EventManager()

      # Registrando os eventos no gerenciador
      event_manager.register_event("MessageEvent", MessageEvent())
      event_manager.register_event("ErrorEvent", ErrorEvent())

      # Criando instâncias dos observadores
      logger = Logger()
      analytics = Analytics()

      # Inscrevendo os observadores aos eventos usando o padrão Observer
      event_manager.subscribe("MessageEvent", logger.log)
      event_manager.subscribe("MessageEvent", analytics.process)
      event_manager.subscribe("ErrorEvent", logger.log)

      # Instanciando o controlador da aplicação, separando a configuração de rotas do restante da lógica
      AppController.setup_routes(self, event_manager)
