from flask import Flask
from src.flask_router import FlaskRouter
from src.event_manager import EventManager
from src.observers.logger import Logger
from src.observers.analytics import Analytics

class App(Flask):
    def __init__(self):
      # --- Configuração do Flask e Eventos ---
      Flask.__init__(self, __name__)

      # Registrando os eventos no gerenciador
      EventManager.register_event("MessageEvent")
      EventManager.register_event("ErrorEvent")

      # Criando instâncias dos observadores
      logger = Logger('logfile.txt') # Este arquivo estaria normalmente em /var/log
      analytics = Analytics()

      # Inscrevendo os observadores aos eventos usando o padrão Observer
      EventManager.subscribe("MessageEvent", logger.message)
      EventManager.subscribe("MessageEvent", analytics.process)
      EventManager.subscribe("ErrorEvent", logger.error)

      # Instanciando o controlador da aplicação, separando a configuração de rotas do restante da lógica
      FlaskRouter.setup_routes(self)
