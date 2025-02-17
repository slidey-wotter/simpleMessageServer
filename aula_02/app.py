from flask import Flask, request, jsonify, send_from_directory

# --- Classes Base para Eventos ---

class BaseEvent:
    """
    Classe base para eventos. 
    Demonstra o conceito de encapsulamento: todos os eventos terão uma estrutura comum.
    """
    def __init__(self, name=""):
        self.name = name
        self.subscribers = []  # Lista de callbacks inscritos no evento
    
    def subscribe(self, callback):
        """Adiciona um callback à lista de inscritos."""
        self.subscribers.append(callback)
    
    def notify(self, data):
        """Notifica todos os inscritos com os dados passados."""
        for callback in self.subscribers:
            callback(data)

# Evento específico para mensagens, utilizando herança da BaseEvent
class MessageEvent(BaseEvent):
    def __init__(self):
        super().__init__(name="MessageEvent")

# Evento específico para erros, também utilizando herança da BaseEvent
class ErrorEvent(BaseEvent):
    def __init__(self):
        super().__init__(name="ErrorEvent")

# --- Gerenciador de Eventos ---
class EventManager:
    """
    Gerencia o registro e a notificação dos eventos.
    Utiliza encapsulamento para ocultar a lógica interna de manipulação dos eventos.
    """
    def __init__(self):
        self.events = {}  # Dicionário para armazenar eventos registrados

    def register_event(self, event_name, event_obj):
        """Registra um evento com um nome identificador."""
        self.events[event_name] = event_obj

    def subscribe(self, event_name, callback):
        """Inscreve um callback em um evento registrado."""
        if event_name in self.events:
            self.events[event_name].subscribe(callback)
        else:
            print(f"[EventManager] Evento '{event_name}' não encontrado.")

    def notify(self, event_name, data):
        """Dispara um evento notificando todos os inscritos."""
        if event_name in self.events:
            self.events[event_name].notify(data)
        else:
            print(f"[EventManager] Evento '{event_name}' não encontrado.")

# --- Observadores (Observers) ---
class Logger:
    """
    Observador que registra (log) os dados recebidos.
    Demonstra o padrão Observer: reage a notificações de eventos.
    """
    def log(self, data):
        print(f"[Logger] Dados recebidos: {data}")

class Analytics:
    """
    Observador que processa os dados para análise.
    Outro exemplo do padrão Observer.
    """
    def process(self, data):
        print(f"[Analytics] Processando dados: {data}")

# --- Controlador da Aplicação ---
class AppController:
    """
    Controlador que centraliza a configuração das rotas do Flask.
    Separa a lógica de configuração das rotas da lógica de negócios, promovendo modularização.
    """
    def __init__(self, app, event_manager):
        self.app = app
        self.event_manager = event_manager
        self.setup_routes()  # Configura as rotas assim que a instância é criada

    def setup_routes(self):
        @self.app.route('/', methods=['GET'])
        def index():
            return send_from_directory('python/static', 'index.html')

        @self.app.route('/send', methods=['POST'])
        def send_message():
            # Extrai o JSON da requisição
            data = request.json
            message = data.get('message', '').strip()
            if not message:
                # Se a mensagem estiver vazia, dispara um evento de erro
                self.event_manager.notify("ErrorEvent", "Mensagem vazia enviada")
                return jsonify({"status": "Erro", "error": "Mensagem vazia"}), 400
            # Dispara o evento de mensagem com o conteúdo recebido
            self.event_manager.notify("MessageEvent", message)
            return jsonify({"status": "Mensagem processada", "message": message})

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
