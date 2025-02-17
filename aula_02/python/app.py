from flask import Flask, request, jsonify

# --- Classes Base para Eventos ---

class BaseEvent:
    def __init__(self, name=""):
        self.name = name
        self.subscribers = []
    
    def subscribe(self, callback):
        """Inscreve um callback para o evento."""
        self.subscribers.append(callback)
    
    def notify(self, data):
        """Notifica todos os inscritos com os dados fornecidos."""
        for callback in self.subscribers:
            callback(data)

# Evento específico para mensagens
class MessageEvent(BaseEvent):
    def __init__(self):
        super().__init__(name="MessageEvent")

# Evento específico para erros
class ErrorEvent(BaseEvent):
    def __init__(self):
        super().__init__(name="ErrorEvent")

# --- Gerenciador de Eventos ---
class EventManager:
    def __init__(self):
        self.events = {}

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
        """Dispara um evento notificando todos os seus inscritos."""
        if event_name in self.events:
            self.events[event_name].notify(data)
        else:
            print(f"[EventManager] Evento '{event_name}' não encontrado.")

# --- Observadores (Observers) ---
class Logger:
    def log(self, data):
        print(f"[Logger] Dados recebidos: {data}")

class Analytics:
    def process(self, data):
        print(f"[Analytics] Processando dados: {data}")

# --- Controlador da Aplicação ---
class AppController:
    def __init__(self, app, event_manager):
        self.app = app
        self.event_manager = event_manager
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/', methods=['GET'])
        def index():
            return "Bem-vindo à aula de Programação Orientada a Objetos II e Flask!"

        @self.app.route('/send', methods=['POST'])
        def send_message():
            data = request.json
            message = data.get('message', '').strip()
            if not message:
                self.event_manager.notify("ErrorEvent", "Mensagem vazia enviada")
                return jsonify({"status": "Erro", "error": "Mensagem vazia"}), 400
            # Dispara o evento de mensagem com a mensagem recebida
            self.event_manager.notify("MessageEvent", message)
            return jsonify({"status": "Mensagem processada", "message": message})

# --- Configuração do Flask e Eventos ---
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
controller = AppController(app, event_manager)

if __name__ == '__main__':
    app.run(debug=True)
